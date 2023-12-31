from django.conf import settings

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Plan, ForeignOrder, Order

from .serializers import (PlanSerializer,
                          CreateUserForOrderSerializer,
                          ForeignOrderSerializer, OrderSerializer)
from .services import (PayPalOrdersMixin,
                       StripePaymentMixin,
                       QuerySetMixin,
                       UserCreateForPaymentMixin, ForeignOrderMixin, OrderMixin)

from apps.users.services import get_jwt_tokens_for_user


# class CreateUserToMakePaymentAPIView(UserCreateForPaymentMixin,
#                                      GenericAPIView):
#     serializer_class = CreateUserForSubscriptionMixin
#     mail_with_celery = False
#
#     def post(self, *args, **kwargs):
#         serializer = self.serializer_class(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#
#         email = serializer.data.get('email')
#         full_name = serializer.data.get('full_name')
#         if not self.check_email_unique(email):
#             return Response({
#                 'error': 'User with provided email is already exists!'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         user = self.create_user_for_email(email, full_name)
#
#         if user is None:
#             return Response({
#                 'error': 'Something went wrong... Please, try again.'
#             }, status=status.HTTP_400_BAD_REQUEST)
#
#         return Response(
#             data=get_jwt_tokens_for_user(user),
#             status=status.HTTP_200_OK
#         )

class ValidateEmailAndFullNameAPIView(UserCreateForPaymentMixin,
                                      GenericAPIView):
    serializer_class = CreateUserForOrderSerializer

    def post(self, *args, **kwargs):
        email = self.request.data.get('email')
        full_name = self.request.data.get('full_name')
        required_fields = [email, full_name]
        for field in required_fields:
            if field == '':
                return Response({
                    'error': 'Email and full name must be provided!'
                }, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        if not self.check_email_unique(email):
            return Response({
                'error': 'User with provided email is already exists!'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not self.check_email_unique_in_order(email):
            return Response({
                'error': 'This email was used in another order!'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreatePayPalOrderAPIView(PayPalOrdersMixin,
                               UserCreateForPaymentMixin,
                               QuerySetMixin,
                               GenericAPIView):
    serializer_class = CreateUserForOrderSerializer

    def post(self, *args, **kwargs):
        plan_id = self.kwargs.get('plan_id')
        if plan_id is None:
            return Response({
                'error': 'You must provide plan ID'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        plan: Plan = self.get_model_instance_by_id(Plan, plan_id)
        if plan is None:
            return Response({
                'error': 'This plan doesn\'t exists!'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        order_creation_data = {
            'plan': plan,
            'status': 'ACTIVE',
            'payment_service': 'PAYPAL',
        }

        if self.request.user.is_authenticated:
            user = self.request.user
            order_creation_data['user'] = user
        else:
            email = self.request.data.get('email')
            full_name = self.request.data.get('full_name')
            required_fields = [email, full_name]

            for field in required_fields:
                if field == '':
                    return Response({
                        'error': 'Email and full name must be provided!'
                    }, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(data=self.request.data)
            serializer.is_valid(raise_exception=True)

            if not self.check_email_unique(email):
                return Response({
                    'error': 'User with provided email is already exists!'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not self.check_email_unique_in_order(email):
                return Response({
                    'error': 'This email was used in another order!'
                }, status=status.HTTP_400_BAD_REQUEST)

            order_creation_data['email'] = serializer.data.get('email')
            order_creation_data['full_name'] = serializer.data.get('full_name')
            order_creation_data['with_user_creation'] = True

        data, error = self.create_order(plan.price)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)
        order_creation_data['paypal_order_id'] = data.get('order_id')

        self.create_order_in_db(order_creation_data)

        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )


class CompleteOrderByPayPalOrderID(PayPalOrdersMixin,
                                   UserCreateForPaymentMixin,
                                   QuerySetMixin,
                                   APIView):
    mail_with_celery = False

    def post(self, *args, **kwargs):
        order_id = self.kwargs.get('order_id')

        if order_id is None:
            return Response({
                'error': 'Order ID must be provided!'
            }, status=status.HTTP_400_BAD_REQUEST)

        order: Order = self.get_order_by_data({'paypal_order_id': order_id})

        if order is None:
            return Response({
                'error': 'No such order with provided order ID.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if order.status != 'ACTIVE':
            return Response({
                'error': 'This order is not active!'
            }, status=status.HTTP_400_BAD_REQUEST)

        data, error = self.capture_order(order_id)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)
        if order.with_user_creation:
            self.create_user_for_order(order)
        self.complete_order(order)

        return Response(data, status.HTTP_200_OK)


class CancelPayPalOrderByIDAPIView(PayPalOrdersMixin,
                                   QuerySetMixin,
                                   APIView):

    def post(self, *args, **kwargs):
        order_id = self.kwargs.get('order_id')

        if order_id is None:
            return Response({
                'error': 'Order ID must be provided!'
            }, status=status.HTTP_400_BAD_REQUEST)

        order: Order = self.get_order_by_data({'paypal_order_id': order_id})

        if order is None:
            return Response({
                'error': 'No such order with provided order ID.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if order.status != 'ACTIVE':
            return Response({
                'error': 'This order is not active!'
            }, status=status.HTTP_400_BAD_REQUEST)

        self.cancel_order_in_db(order)
        return Response({
            'success': 'Order was successfully canceled'
        }, status=status.HTTP_200_OK)


class StripeConfigAPIView(APIView):

    def get(self, *args, **kwargs):
        config = {'public_key': settings.STRIPE_PUBLISHABLE_KEY}
        return Response(config, status=status.HTTP_200_OK)


class CreateStripeCheckoutSessionAPIView(StripePaymentMixin,
                                         UserCreateForPaymentMixin,
                                         QuerySetMixin,
                                         APIView):
    serializer_class = CreateUserForOrderSerializer

    # permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        plan_id = self.kwargs.get('plan_id')
        if plan_id is None:
            return Response({
                'error': 'You must provide plan ID'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        plan: Plan = self.get_model_instance_by_id(Plan, plan_id)
        if plan is None:
            return Response({
                'error': 'This plan doesn\'t exists!'  # noqa
            }, status=status.HTTP_400_BAD_REQUEST)

        user_id = None
        order_with_user_creation = False
        order_user_creation_data = None
        if self.request.user.is_authenticated:
            user = self.request.user
            user_id = user.id
        else:
            email = self.request.data.get('email')
            full_name = self.request.data.get('full_name')
            required_fields = [email, full_name]

            for field in required_fields:
                if field == '':
                    return Response({
                        'error': 'Email and full name must be provided!'
                    }, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.serializer_class(data=self.request.data)
            serializer.is_valid(raise_exception=True)

            if not self.check_email_unique(email):
                return Response({
                    'error': 'User with provided email is already exists!'
                }, status=status.HTTP_400_BAD_REQUEST)

            if not self.check_email_unique_in_order(email):
                return Response({
                    'error': 'This email was used in another order!'
                }, status=status.HTTP_400_BAD_REQUEST)
            order_with_user_creation = True
            order_user_creation_data = {
                'email': email,
                'full_name': full_name,
                'with_user_creation': True
            }
        checkout_session_id = self.create_checkout_session(
            client_id=user_id,
            plan=plan,
            order_with_user_creation=order_with_user_creation,
            order_user_creation_data=order_user_creation_data
        )
        if checkout_session_id is None:
            return Response({
                'error': 'Something went wrong with payment, please try again!'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'checkout_session_id': checkout_session_id
        }, status=status.HTTP_201_CREATED)


class CreateStripeForeignCheckoutSessionAPIView(ForeignOrderMixin,
                                                StripePaymentMixin,
                                                GenericAPIView):
    serializer_class = ForeignOrderSerializer
    foreign_order = True

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        order: ForeignOrder = serializer.save()

        checkout_session_id = self.create_checkout_session(
            client_id=order.email,
            foreign_order=order
        )
        if checkout_session_id is None:
            return Response({
                'error': 'Something went wrong with payment, please try again!'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'checkout_session_id': checkout_session_id
        }, status=status.HTTP_201_CREATED)


class StripeWebhookAPIView(StripePaymentMixin,
                           QuerySetMixin,
                           APIView):
    mail_with_celery = False

    def post(self, *args, **kwargs):
        payload = self.request.body
        sig_header = self.request.META['HTTP_STRIPE_SIGNATURE']
        self.complete_payment(payload, sig_header)
        return Response(data={'data': True})


class StripeSuccessAPIView(OrderMixin,
                           QuerySetMixin,
                           APIView):

    def post(self, *args, **kwargs):
        success_id = self.kwargs.get('success_id')

        if success_id is None:
            return Response({
                'error': 'Wrong success ID'
            }, status=status.HTTP_400_BAD_REQUEST)
        order = self.get_order_by_data({'stripe_success_id': success_id})
        if order is None:
            return Response({
                'error': 'No such order with provided cancel ID'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'success': 'Successful payment',
            'order_id': order.id
        }, status=status.HTTP_200_OK)


class StripeForeignSuccessAPIView(StripeSuccessAPIView):

    def post(self, *args, **kwargs):
        response = super().post(*args, **kwargs)

        if response.status_code == 200:
            order = self.get_order_by_data({'id': response.data['order_id']})
            response.data['success_url'] = order.success_url
        return response


class StripeCancelOrderAPIView(StripePaymentMixin,
                               QuerySetMixin,
                               APIView):

    def post(self, *args, **kwargs):
        cancel_id = self.kwargs.get('cancel_id')

        if cancel_id is None:
            return Response({
                'error': 'Wrong cancel ID'
            }, status=status.HTTP_400_BAD_REQUEST)

        order = self.get_order_by_data({'stripe_cancel_id': cancel_id})
        if order is None:
            return Response({
                'error': 'No such order with provided cancel ID'
            }, status=status.HTTP_400_BAD_REQUEST)

        self.cancel_order(order, cancel_id)
        return Response({
            'success': 'Order was successfully canceled'
        }, status=status.HTTP_200_OK)


class StripeCancelForeignOrderAPIView(StripePaymentMixin,
                                      QuerySetMixin,
                                      APIView):

    def post(self, *args, **kwargs):
        cancel_id = self.kwargs.get('cancel_id')

        if cancel_id is None:
            return Response({
                'error': 'Wrong cancel ID'
            }, status=status.HTTP_400_BAD_REQUEST)

        order = self.get_order_by_data({'stripe_cancel_id': cancel_id})
        if order is None:
            return Response({
                'error': 'No such order with provided cancel ID'
            }, status=status.HTTP_400_BAD_REQUEST)

        if order.is_ended:
            return Response({
                'error': 'This order is not active!'
            }, status=status.HTTP_400_BAD_REQUEST)

        self.cancel_order(order, cancel_id)
        return Response({
            'success': 'Order was successfully canceled',
            'cancel_url': order.cancel_url
        }, status=status.HTTP_400_BAD_REQUEST)


class PlansAPIVIew(ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDetailAPIView(RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class CreatePayPalForeignOrderAPIView(PayPalOrdersMixin,
                                      GenericAPIView):
    serializer_class = ForeignOrderSerializer
    foreign_order = True

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        order: ForeignOrder = serializer.save()

        data, error = self.create_order(
            order.amount,
            success_url=settings.PAYPAL_FOREIGN_SUCCESS_URL,
            cancel_url=settings.PAYPAL_FOREIGN_CANCEL_URL
        )

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)

        order.paypal_order_id = data.get('order_id')
        order.save()

        return Response(
            data=data,
            status=status.HTTP_201_CREATED
        )


class CompleteForeignOrderByPayPalOrderID(ForeignOrderMixin,
                                          APIView):
    foreign_order = True

    def post(self, *args, **kwargs):
        order_id = self.kwargs.get('order_id')

        if order_id is None:
            return Response({
                'error': 'Order ID must be provided!'
            }, status=status.HTTP_400_BAD_REQUEST)

        data, error = self.foreign_paypal_capture(order_id)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status.HTTP_200_OK)


class CancelForeignOrderByPayPalOrderID(ForeignOrderMixin,
                                        APIView):
    foreign_order = True

    def post(self, *args, **kwargs):
        order_id = self.kwargs.get('order_id')

        if order_id is None:
            return Response({
                'error': 'Order ID must be provided!'
            }, status=status.HTTP_400_BAD_REQUEST)

        order: Order | ForeignOrder = self.get_order_by_data({'paypal_order_id': order_id})

        if order is None:
            return Response({
                'error': 'No such order with provided order ID.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if order.is_ended:
            return Response({
                'error': 'This order is not active!'
            }, status=status.HTTP_400_BAD_REQUEST)

        self.make_order_ended(order)
        data, error = self.cancel_foreign_order(order)

        if error is not None:
            return Response({
                'error': error
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=data, status=status.HTTP_200_OK)


class UserOrders(OrderMixin,
                 GenericAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        orders = self.get_user_orders(self.request.user)
        serializer = self.serializer_class(many=True, instance=orders)
        return Response(serializer.data, status=status.HTTP_200_OK)

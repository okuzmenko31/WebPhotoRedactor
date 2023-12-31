from datetime import datetime

from rest_framework import serializers

from .models import Plan, ForeignOrder, Order


class CreateUserForOrderSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=150,
                                      required=False,
                                      label='Full name')
    email = serializers.EmailField(required=False,
                                   label='Email for account creation')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price',
                  'bg_deletions_count', 'up_scales_count',
                  'jpg_artifacts_deletions_count', 'stripe_price_id']


# class CreateUserForOrderSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=False)
#     full_name = serializers.CharField(max_length=150,
#                                       required=False,
#                                       label='Full name')


class ForeignOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignOrder
        fields = '__all__'
        read_only_fields = ['paypal_order_id', 'stripe_session_id', 'is_ended',
                            'stripe_cancel_id', 'stripe_success_id']


class OrderSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    parsed_created_at = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'plan', 'status',
                  'payment_service', 'parsed_created_at',
                  'created_at', 'stripe_cancel_id', 'stripe_success_id']

    @staticmethod
    def get_parsed_created_at(instance: Order):
        created_at = str(instance.created_at)
        parsed_date = datetime.fromisoformat(
            created_at.replace('T', ' ').split('+')[0])
        formatted_date = parsed_date.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date

from rest_framework.generics import ListAPIView, CreateAPIView

from .models import *
from .serializers import (MainFaqSerializer,
                          PricingFaqSerializer,
                          HelpRequestSerializer)


class MainFaqListAPIView(ListAPIView):
    serializer_class = MainFaqSerializer
    queryset = MainFaq.objects.all()


class PricingFaqListAPIView(ListAPIView):
    serializer_class = PricingFaqSerializer
    queryset = PricingFaq.objects.all()


class CreateRequestAPIView(CreateAPIView):
    serializer_class = HelpRequestSerializer
    queryset = HelpRequest.objects.all()

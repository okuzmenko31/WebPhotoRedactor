from rest_framework.generics import ListAPIView

from .models import *
from .serializers import MainFaqSerializer, PricingFaqSerializer


class MainFaqListAPIView(ListAPIView):
    serializer_class = MainFaqSerializer
    queryset = MainFaq.objects.all()


class PricingFaqListAPIView(ListAPIView):
    serializer_class = PricingFaqSerializer
    queryset = PricingFaq.objects.all()

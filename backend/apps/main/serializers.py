from rest_framework import serializers

from .models import *


class MainFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainFaq
        fields = '__all__'


class PricingFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingFaq
        fields = '__all__'

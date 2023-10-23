from django.urls import path

from .views import *

urlpatterns = [
    path('main_faqs/', MainFaqListAPIView.as_view()),
    path('pricing_faqs/', PricingFaqListAPIView.as_view()),
    path('help_request/', CreateRequestAPIView.as_view())
]

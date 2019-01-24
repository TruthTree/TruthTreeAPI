from .views import (
    StateRevenueApiView,
    CountyRevenueApiView
)
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('state_revenue/', StateRevenueApiView, name='revenue-data-api'),
    path('county_revenue/', CountyRevenueApiView, name='revenue-data-api')
]

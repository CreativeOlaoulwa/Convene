from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .api_views import (
    EventListAPIView,
    EventDetailAPIView,
    RegistrationCreateAPIView,
    RegistrationDeleteAPIView,
)

urlpatterns = [
    path('events/', EventListAPIView.as_view(), name='api_event_list'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='api_event_detail'),
    path('registrations/', RegistrationCreateAPIView.as_view(), name='api_registration_create'),
    path('registrations/<int:pk>/', RegistrationDeleteAPIView.as_view(), name='api_registration_delete'),
    path('token/', obtain_auth_token, name='api_token'),
]
from django.urls import path
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
]
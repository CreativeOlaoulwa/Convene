from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('events/<int:pk>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/register/', views.register_for_event, name='register_for_event'),
    path('my-registrations/', views.my_registrations, name='my_registrations'),
    path('registrations/<int:pk>/cancel/', views.cancel_registration, name='cancel_registration'),
    path('events/<int:pk>/checkin/', views.event_checkin, name='event_checkin'),
]
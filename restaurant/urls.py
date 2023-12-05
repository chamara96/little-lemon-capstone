from django.contrib import admin
from django.urls import path
from .views import MenuItemView, SingleMenuItemView, BookingViewSet



urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
]

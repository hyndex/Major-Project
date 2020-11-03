from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', ProfileViewSet)
router.register(r'charger', ChargerViewSet)
router.register(r'booking', BookingViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('changePassword/', ChangePasswordView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('login/', LoginView.as_view()),
    path('upload/', picUploadView.as_view()),
]
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission
from django.db.models import Q
from .models import *


class ProfilePermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.method =='POST':
            return True
        if request.user.is_authenticated:
            if request.method in ['GET','DELETE','PUT']:
                return True
        return False

def ProfileQuerySet(request):
    return Profile.objects.filter(user__username=request.user.username)


class ChargerPermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','GET','DELETE','PUT']:
                return True
        return False

def ChargerQuerySet(request):
    return Charger.objects.filter(profile__user__username=request.user.username)


class BookingPermission(BasePermission):
    message='You are not authorized to this data'
    def has_permission(self, request, view):
        SAFE_METHOD = ['GET','POST','PUT','DELETE']
        if request.method not in SAFE_METHOD:
            return False
        if request.user.is_authenticated:
            if request.method in ['POST','GET','DELETE','PUT']:
                return True
        return False

def BookingQuerySet(request):
    return Charger.objects.filter(profile__user__username=request.user.username)

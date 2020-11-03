from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser, FileUploadParser
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
# from sorl.thumbnail import get_thumbnail


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    search_fields = ['user__username','user__email','phone','name']
    filter_backends = (filters.SearchFilter,)
    parser_classes=(FormParser, MultiPartParser,JSONParser)

    serializer_class = ProfileSerializer
    permission_classes = [ProfilePermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return ProfileQuerySet(self.request)

class ChargerViewSet(viewsets.ModelViewSet):
    queryset = Charger.objects.all()
    search_fields = ['user__username','user__email','name']
    filter_backends = (filters.SearchFilter,)
    parser_classes=(FormParser, MultiPartParser,JSONParser)

    serializer_class = ChargerSerializer
    permission_classes = [ChargerPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return ChargerQuerySet(self.request)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    search_fields = ['user__username','user__email','charger__name','charger__id']
    filter_backends = (filters.SearchFilter,)
    parser_classes=(FormParser, MultiPartParser,JSONParser)

    serializer_class = BookingSerializer
    permission_classes = [BookingPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return BookingQuerySet(self.request)
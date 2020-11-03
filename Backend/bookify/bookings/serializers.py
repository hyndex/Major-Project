from rest_framework import serializers
from rest_framework import exceptions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from .permissions import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','password','email')
        write_only_fields=('password',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Profile
        fields = ('id','user','name','phone','address','status','image')
        read_only_fields=('image',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(username=str(user_data['username']).lower(),
                            email=str(user_data['email']).lower(),
                            )
        user.set_password(user_data['password'])
        user.save()
        try:
            profile = Profile.objects.create(user=user,
                                phone=validated_data.pop('phone'),
                                address=validated_data.pop('address'),
                                status=validated_data.pop('status'),
                                )
            return profile
        except:
            User.objects.filter(username=user_data['username']).delete()
        return {"False"}


class ChargerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charger
        fields=('id','address','status','date_updated','profile')
        read_only_fields=('id','date_updated','profile')

    def create(self, validated_data):
        user= Profile.objects.get(user=self.context['request'].user)
        charger=Charger.objects.create(user=user,**validated_data)
        return charger


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields=('id','profile','status','charger','date_updated')
        read_only_fields=('date_updated','profile','id',)
    
    def create(self, validated_data):
        profile=Profile.objects.get(user=self.context['request'].user)
        booking=Booking.objects.create(profile=profile,**validated_data)
        return booking




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username','')
        password = data.get('password','')

        if username and password:#checking if both are avalable or not
            user = authenticate(username=username,password=password)
            if user:# if user found 
                if user.is_active:# if user is active
                    data['user'] = user #if all correct then we are going to add "user" to given "data" and return 
                else:#if account is not active reise or active the account
                    msg = 'account is not active'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'unable to login with given creds'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Username or Passwords are both required !!!'
            raise exceptions.ValidationError(msg)
        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


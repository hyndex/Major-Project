from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime as dt




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=True, default = '')
    phone = models.CharField(max_length=20, blank=False, null=True, default = '')
    address = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to='',blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.user.username

class Charger(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)  
    address = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)
    
    def __str__(self):
        return self.user.username


class Bookings(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    charger=models.ForeignKey(Charger, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, blank=True, null=True)
    date_updated = models.DateTimeField(default=dt.datetime.now(), blank=True)  
    def __str__(self):
        return str(self.user.user.username+' '+self.charger.id+' '+self.date_updated)


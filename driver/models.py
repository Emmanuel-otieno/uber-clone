from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.utils import timezone
from django.db import models
import datetime as dt
import cloudinary

# Create your models here.
class Driver(models.Model):

    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio =  HTMLField(blank=True)
    avatar = CloudinaryField('image', blank=True, null=True)
    pickup_location = models.ForeignKey('app.location', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    def __str__(self):
        return self.name

    def save_driver(self):
        self.save()

    def delete_driver(self):
        self.delete()
    



class Location (models.Model):

    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    location_name = models.ForeignKey('app.Driver', on_delete=models.CASCADE)
    category = models.ForeignKey('app.Category', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()   

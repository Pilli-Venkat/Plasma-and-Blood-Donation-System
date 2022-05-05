from django.db import models
from django.conf import settings
#from autoslug import AutoslugField
from datetime import datetime

import uuid

from django.contrib.auth.models import User

class Donate(models.Model):

    donate_id= models.UUIDField(default = uuid.uuid4)

    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
   # slug=AutoslugField(populate_from='name',)
    age = models.IntegerField(null=False,blank=False)
    gender = models.CharField(max_length=10)
    choose = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    state = models.CharField(max_length=100)
    mobile= models.IntegerField(null=False,blank=False)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250,null=False,blank=False)
    district = models.CharField(max_length=250,null=False,blank=False)

  #  description = models.CharField(null=True, blank=True, max_length=250)

    issues = models.CharField(null=True, blank=True,max_length=250)
    
    posted_at = models.DateField(default=datetime.now,null=True,blank=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['-posted_at',]


    def __str__(self):
        return self.email


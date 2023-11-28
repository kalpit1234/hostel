from django.db import models
from django.contrib.auth.models import User
from datetime import date    
class Contactus(models.Model):
    full_name=models.CharField(default='kal',max_length=300,null=True)
    email=models.EmailField(default="kalpitmathur3@gmail.com",max_length=300,null=True)
    message=models.CharField(default="kfek",max_length=400,null=True)
    
    def __str__(self):
        return self.full_name
    
class Profile(models.Model):
       user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
       first_name=models.CharField(default="harshagarwal",max_length=400,null=True)
       last_name=models.CharField(default="harsh",max_length=400,null=True)
       def  __str__(self):
           return str(self.user)

from django.db import models
from django.utils import timezone

class Book(models.Model):
    state = models.CharField(default='pappu', max_length=45, null=True)
    check_in = models.DateTimeField(default=timezone.now, blank=True, null=True)
    check_out = models.DateTimeField(default=timezone.now, blank=True, null=True)
    Adults = models.IntegerField(default=11, null=True)
    children = models.IntegerField(default=111, null=True)
    phone_no = models.CharField(max_length=20, default='98234556677', null=True)

    def __str__(self):
        return str(self.state)


    
    
                    
    
    
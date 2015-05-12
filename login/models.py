from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class User(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=150)

    def __str__(self):
	return self.Username

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    Firstname = models.CharField(max_length=100)
    Lastname  = models.CharField(max_length=100)
    Enroll = models.IntegerField(default=0,validators=[MaxValueValidator(99999999),MinValueValidator(1)])
    email = models.EmailField(max_length=75)

class UserImages(models.Model):
    user = models.ForeignKey(User)
    path = '/media/pics/'
    Profilepic = models.FileField(upload_to=(path+'dp/'),max_length=100)
    Coverpic = models.FileField(upload_to=(path+'cp/'),max_length=100)





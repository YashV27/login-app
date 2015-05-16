from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class User(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=150)

    def __str__(self):
	return self.Username

	first_login = True 
	
class UserInfo(models.Model):
    user = models.ForeignKey(User)
    Firstname = models.CharField(max_length=100)
    Lastname  = models.CharField(max_length=100)
    Enroll = models.IntegerField(default=0,validators=[MaxValueValidator(99999999),MinValueValidator(1)])
    email = models.EmailField()

class UserImages(models.Model):
    user = models.ForeignKey(User)
    Profilepic = models.FileField(upload_to=('dp/'),max_length=100)
    Coverpic = models.FileField(upload_to=('cp/'),max_length=100)





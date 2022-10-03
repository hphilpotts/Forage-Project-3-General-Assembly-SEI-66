
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

# image model
class Image(models.Model):
    img = models.ImageField(upload_to = 'main_app/static/uploads', default="")
    subject = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
  



class Board(models.Model):
    author=models.ForeignKey( User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    subject= models.CharField(max_length=250)
    # images= models.ManyToManyField(Image)
    date = models.DateField('Created At')

    def __str__(self):
        return self.subject
   


    def __str__(self):
        return self.subject






# user profile model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_bio = models.TextField(max_length=500)
    user_profile_pic = models.ImageField(upload_to='profilepics')
        # My understanding is that Django saves locally by default:
        # path should be something like '/media/profilepics/<filename>.jpg' or similar
        # may need to make changes to naming and storage, see https://docs.djangoproject.com/en/4.1/topics/files/
# authentication model 

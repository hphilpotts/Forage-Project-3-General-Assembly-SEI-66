
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

from datetime import date
from django.utils.timezone import now


# Create your models here.

# image model
class Image(models.Model):

    img = models.ImageField(upload_to = 'main_app/static/uploads', default="", blank= TRUE )
    subject = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
     return reverse('images_detail', kwargs = {'pk': self.id})
  



class Board(models.Model):
    title = models.CharField(max_length=250)
    subject= models.CharField(max_length=250)
    images= models.ManyToManyField(Image)
    date = models.DateField('Created At', default=now, editable=False)
    user = models.ForeignKey( User, on_delete=models.CASCADE)

    def get_absolute_url(self):
     return reverse('board_detail', kwargs = {'board_id': self.id})


    def __str__(self):
        return self.subject






# user profile model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_bio = models.TextField(max_length=500)
    user_profile_pic = models.ImageField(default='no image', upload_to='profilepics')
        # My understanding is that Django saves locally by default:
        # path should be something like '/media/profilepics/<filename>.jpg' or similar
        # may need to make changes to naming and storage, see https://docs.djangoproject.com/en/4.1/topics/files/

    def __str__(self):
        return self.user.username
            # Friendly return value

    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.user_profile_pic.path)

    #     if img.height > 100 or img.width> 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)

# authentication model 

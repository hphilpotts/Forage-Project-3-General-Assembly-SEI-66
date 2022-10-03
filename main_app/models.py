
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# image model









# board model 

class Board(models.Model):
    author=models.ForeignKey( User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    subject= models.CharField(max_length=250)
    # images= models.ManyToManyField(Image)
    date = models.DateField('Created At')

    def __str__(self):
        return self.subject
   








# user profile model 





# authentication model 
from django.db import models
from django.urls import reverse

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
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})




# board model 









# user profile model 





# authentication model 




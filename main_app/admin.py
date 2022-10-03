from django.contrib import admin

from .models import Image
from .models import Board





# Register your models here.

admin.site.register(Board)
admin.site.register(Image)



class List:
    def remove_(self, integer_list, values_list):
        arr = [i for i in integer_list if i not in values_list]
        return arr


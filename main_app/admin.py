from django.contrib import admin

from .models import Board, Image , Profile






# Register your models here.

admin.site.register(Board)
admin.site.register(Image)
admin.site.register(Profile)





class List:
    def remove_(self, integer_list, values_list):
        arr = [i for i in integer_list if i not in values_list]
        return arr


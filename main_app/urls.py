from django.urls import path
from . import views

urlpatterns =[
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
   
     # image urls 










     # userprofile urls 



     

    # authenitcation urls 








     # board urls 
     path('boards/', views.boards_index, name='index')



    






]
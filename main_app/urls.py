from django.urls import path
from . import views

urlpatterns =[
     path('', views.home, name='home'),
     path('about/', views.about, name='about'),
   
     # image urls 

    path('images/', views.images_index, name='index'),
    path('images/<int:image_id>', views.images_detail, name='detail'),
    path('images/create/', views.ImageCreate.as_view(), name='images_create'),
    path('images/<int:pk>/update/', views.ImageUpdate.as_view(), name='images_update'),
    path('images/<int:pk>/delete/', views.ImageDelete.as_view(), name='images_delete'),
    path('images/<int:image_id>/add_to_board/', views.add_to_board, name='add_to_board'),











     # userprofile urls 



     

    # authenitcation urls 








     # board urls 
     path('boards/', views.boards_index, name='index')



    






]
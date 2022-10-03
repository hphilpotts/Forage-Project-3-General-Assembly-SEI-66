from django.shortcuts import render
from django.http import HttpResponse

from main_app.models import Board


# Define the home view:
def home(request):

  return render(request, 'home.html')

# Define about view:
def about(request):
  return render(request, 'about.html')


     # image views










     # userprofile views



     

    # authenitcation views








     # board views 

def boards_index(request):
  
  boards = Board.objects.all()
  return render(request, 'boards/index.html', {'boards': boards})
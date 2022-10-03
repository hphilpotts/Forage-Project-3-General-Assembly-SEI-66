from django.shortcuts import render
from django.http import HttpResponse


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
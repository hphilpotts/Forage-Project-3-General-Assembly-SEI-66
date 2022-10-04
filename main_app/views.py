import profile
from django.shortcuts import render, redirect


from .models import Image, Board
from .forms import ProfileForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Board, User, Profile

# Create your views here.
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# Define the home view:
def home(request):

  return render(request, 'home.html')

# Define about view:
def about(request):
  return render(request, 'about.html')

     # image views
class ImageCreate(CreateView):
    model = Image
    fields = ['img', 'subject', 'description', ] # All fields mentioned in models.py file
    success_url = '/images/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ImageUpdate(UpdateView):
    model = Image
    fields = ['img', 'subject', 'description', ]
class ImageDelete(DeleteView):
    model = Image
    success_url = 'images/index.html/'


# def image_Index(request):
   
#     return render(request, 'images/index.html')
def image_Index(request):
    images = Image.objects.filter()
    return render(request, 'images/index.html', { 'images': images})

def images_detail(request, image_id):
    # SELECT * FROM main_app_image WHERE id = image_id
    image = Image.objects.get(id = image_id)

def add_to_board(request, image_id):
    return redirect('detail', image_id = image_id)


     # userprofile views
def profile_detail(request, user_id):
    user = User.objects.get(id = user_id)
    profile_form = ProfileForm()
    return render(request, 'profiles/detail.html', {'user': user, 'profile-form': profile_form})

# def profile_update(request, user_id):
#      user - User.objects.get(id = user_id)
#      form = ProfileForm(request.POST)
#      if form.is_valid():
#       user.save()
#     return 


    # authenitcation views
def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about') # change this once index or profile is added
        else:
            error_message = "Invalid signup - Please try again later"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)


class BoardCreate(CreateView):
    model = Board
    fields = [ 'title', 'subject']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BoardUpdate(UpdateView):
    model = Board
    fields = [ 'title', 'subject']


class BoardDelete(DeleteView):
    model = Board
    success_url = '/boards/'

def boards_index(request):
  boards = Board.objects.all()
  return render(request, 'boards/index.html', {'boards': boards})
     # board views 

def boards_detail(request, board_id,):
    board = Board.objects.get(id = board_id)
   
    return render(request, 'boards/detail.html', {'board': board})



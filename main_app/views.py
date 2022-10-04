import profile
from django.shortcuts import render, redirect
from .models import Image
from .forms import UpdateProfileForm, UpdateUserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from main_app.models import Board, User, Profile

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
    fields = ['img', 'subject', 'description', 'created_at',] # All fields mentioned in models.py file
    # success_url = '/cats/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ImageUpdate(UpdateView):
    model = Image
    fields = ['breed', 'description', 'age']

class ImageDelete(DeleteView):
    model = Image
    success_url = '/images/'

def home(request):
    # return HttpResponse('<h1> Hello Cat Collector </h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def images_index(request):
    images = Image.objects.filter(user = request.user)
    return render(request, 'images/index.html', { 'images': images})

def images_detail(request, image_id):
    # SELECT * FROM main_app_cat WHERE id = cat_id
    image = Image.objects.get(id = image_id)

def add_to_board(request, image_id):
    return redirect('detail', image_id = image_id)

# User Profile views:
def profile_detail(request, user_id):
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)
        profile_form.fields['user_bio'].initial = user.profile.user_bio
        profile_form.fields['user_profile_pic'].initial = user.profile.user_profile_pic

    return render(request, 'profiles/detail.html', {'user': user, 'user_form': user_form, 'profile_form': profile_form})

# -- Earlier attempt - not working! --  
# def profile_detail(request, user_id):
#     error_message = ""
#     if request.method == 'POST':
#         # profile_form = ProfileForm(request.POST, request.FILES)
#         pass

#         # if profile_form.is_valid():
#         #     profile_form.save()
#         #     # messages.success(request, 'Updated successfully!')
#         #         # import from django.contrib : messages
#         #     return redirect(to='profile_detail')
    
#     user = User.objects.get(id = user_id)   
#     profile_form = UpdateProfileForm(instance=user)
#     user_form = UpdateUserForm(instance=user)
#     return render(request, 'profiles/detail.html', context={'user': user, 'profile-form': profile_form, 'user_form': user_form})

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

def boards_index(request):
  boards = Board.objects.all()
  return render(request, 'boards/index.html', {'boards': boards})
     # board views 

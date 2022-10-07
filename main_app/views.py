from django.shortcuts import render, redirect

# User messages, emails to user:
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Image, Board
from .forms import ImageForm, UpdateProfileForm, UpdateUserForm, UserSignupForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm

from main_app.models import Board, User

# Authorization imports:
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required # ! required before deployment
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Define the home view:
def home(request):
    messages.info(request, 'Welcome to the Forage App Homepage!') # TODO: remove before deployment
    return render(request, 'home.html')

# Define about view:
def about(request):
  return render(request, 'about.html')

     # image views
class ImageCreate(LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Image
    fields = ['img', 'subject', 'description', ] # All fields mentioned in models.py file
    success_url = '/images/'
    success_message = 'Image created successfully!'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
     

class ImageUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Image
    fields = ['img', 'subject', 'description', ]
    success_url = '/images/'
    success_message = 'Imagee updated successfully!'

class ImageDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Image
    success_url = '/images/'
    success_message = 'Image deletec successfully!'



# def image_Index(request):
   
#     return render(request, 'images/index.html')
@login_required
def image_Index(request):
    images = Image.objects.filter()
    return render(request, 'images/index.html', { 'images': images})




@login_required
def images_detail(request, image_id):
    # SELECT * FROM main_app_image WHERE id = image_id
    image = Image.objects.get(id = image_id)
    return render(request, 'images/detail.html', {'image': image})



@login_required
def add_to_board(request, image_id):
    return redirect('detail', image_id = image_id)

# User Profile views:

# READ (Index):
@staff_member_required # protected route: staff only
def profile_index(request):
    users = User.objects.all()
    return render(request, 'profiles/index.html', {'users': users})

# READ (Detail) with UPDATE form:
@login_required
    # This is not enough protection on its own as users could manually enter urls to edit other users, see check two lines below:
def profile_detail(request, user_id):
    user = User.objects.get(id = user_id)
    boards = Board.objects.filter(user = request.user)
    # Below checks if logged in user's id matches the id of the user being edited, if not this redirects to home.
    # This prevents manual url entry in order to edit other users!    
    if user.id != request.user.id:
        return redirect('home')
    # If there is a match, below code can run to POST or GET the User Profile Detail page (with UPDATE form).
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "User updated successfully.")
            return redirect('profile_detail', user_id = user_id)
        else:
            messages.error(request, "User has not been updated, please try again.")

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)
        profile_form.fields['user_bio'].initial = user.profile.user_bio
        profile_form.fields['user_profile_pic'].initial = user.profile.user_profile_pic

    return render(request, 'profiles/detail.html', {'user': user, 'user_form': user_form, 'profile_form': profile_form, 'boards': boards})

# READ (Detail) other User Profile:
@login_required
def profile_viewer(request, user_id):
    user = User.objects.get(id = user_id)
    boards = Board.objects.filter(user = user.id)
    return render(request, 'profiles/view.html', {'user': user, 'boards': boards})


# DELETE
@login_required
def profile_delete(request, user_id):
    if user_id != request.user.id:
        return redirect('home')
    user = User.objects.get(id = user_id)
    user.delete()
    messages.warning(request, "User has been deleted.")
    return redirect('home')

# Confirm Delete Page:
@login_required
def profile_confirm_delete(request, user_id):
    user = User.objects.get(id = user_id)
    messages.warning(request, "Deleting user...are you sure?")
    return render(request, 'profiles/confirm_delete.html', {'user': user})

# -- Authentication views:

# Signup:
def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign up successful! Add more details in your User Profile page.")
            return redirect('profile_detail', user_id = user.id) # change this once index or profile is added
        else:
            error_message = 'Invalid signup - Please try again later'
            messages.error(request, error_message)
    form = UserSignupForm()
    context = {'form': form, 'error_message': error_message }
    return render(request, 'registration/signup.html', context)

# Change password:
def change_password(request):
    error_message = ""
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Password change (probably) successful!")
            return redirect('profile_detail', user_id = request.user.id)
        else:
            messages.error(request, "Error in changing password.")
    form = PasswordChangeForm(user=request.user)
    context = {'form': form, 'error_message': error_message }
    return render(request, 'passwords/change_password.html', context)



# --------------------


class BoardCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Board
    fields = [ 'title', 'subject' ]
    success_message = 'Board created successfully!'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BoardUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Board
    fields = [ 'title', 'subject']
    success_message = 'Board updated successfully!'



class BoardDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Board
    success_url = '/boards/'
    success_message = 'Board deleted successfully!'


@login_required
def boards_index(request):
  boards = Board.objects.all()
  return render(request, 'boards/index.html', {'boards': boards})
     # board views 

@login_required
def boards_detail(request, board_id,):
    board = Board.objects.get(id = board_id)
    image= Image.objects.exclude(id__in= board.images.all().values_list('id'))
    image_form =ImageForm()
   
    return render(request, 'boards/detail.html', {'board': board, 'image': image , 'image_form': image_form})

@login_required
def add_image(request, board_id):
    print('add image fire')
    print(request.POST)
    form = ImageForm(request.POST, request.FILES)
     
    if form.is_valid():
        print(' image form valid')
        new_image = form.save(commit =False)
        form.instance.user = request.user
        new_image.save()
        messages.success(request, "Image uploaded!")

    return add_image_board(request, board_id = board_id, image_id=new_image.id)

    # else:
    #  print('no image fired')
    #  return None

@login_required
def add_image_board(request, board_id , image_id):
    Board.objects.get(id = board_id).images.add(image_id)
    return redirect('board_detail', board_id =board_id)


@login_required
def assoc_image(request , board_id, image_id):

     Board.objects.get(id = board_id).images.add(image_id)
     messages.success(request, "Image has been added!")

     return redirect('board_detail', board_id =board_id)

@login_required
def unassoc_image(request , board_id, image_id):

    
    Board.objects.get(id = board_id).images.remove(image_id)
    messages.warning(request, "Image removed!")

    return redirect('board_detail', board_id = board_id)



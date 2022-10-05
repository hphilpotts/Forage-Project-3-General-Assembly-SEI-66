from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile , Image

# Edit User form - currently working: renders and saves.
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# Edit Profile form - not working: will not render, not tested if saves.
class UpdateProfileForm(ModelForm):
    user_bio = forms.CharField()
    user_profile_pic = forms.ImageField()

    class Meta:
        model = Profile
        fields = ['user_bio', 'user_profile_pic']


class ImageForm(ModelForm):

    # img = forms.ImageField()
    # subject = forms.CharField(max_length=25)
    # description = forms.CharField(max_length=250)

    class Meta:
        model = Image
        fields = '__all__'



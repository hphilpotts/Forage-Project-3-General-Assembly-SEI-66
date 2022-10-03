from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile



# Edit Profile form - placeholder for now.
# Does not yet work, trying manual forms.
class ProfileForm(forms.ModelForm):
    user_profile_pic = forms.ImageField()
    user_bio = forms.CharField(max_length=500)

    class Meta:
        model = Profile
        fields = ['user_profile_pic', 'user_bio']




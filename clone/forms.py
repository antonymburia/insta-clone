from .models import  Post,Profile
from django import forms
# from django.contrib.auth.models import User

class NewPostForm(forms.ModelForm):
 
    class Meta:
        model = Post
        exclude = ['user', 'pub_date','likes', 'unlikes','comments']

class CreateUserForm(forms.ModelForm):
    class Meta:
        widgets = {
        'password': forms.PasswordInput(),
    }
        model = Profile
        exclude = ['user_id','posts']

        
class ProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = Profile

        exclude = ['posts', 'email','user_id']
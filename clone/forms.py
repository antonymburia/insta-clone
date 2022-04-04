from .models import  Post,User
from django import forms
# from django.contrib.auth.models import User

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date','likes', 'unlikes','comments']
        
class ProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = User

        exclude = ['posts', 'email','user_id']
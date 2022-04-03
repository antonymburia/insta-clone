from .models import  Post,User
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date','likes', 'unlikes','comments']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']
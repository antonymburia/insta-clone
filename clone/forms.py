from .models import  Post,Comment
from django import forms
from django.contrib.auth.models import User

class NewPostForm(forms.ModelForm):
 
    class Meta:
        model = Post
        exclude = [ 'pub_date','liked', 'comments']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        
        
class CreateUserForm(forms.ModelForm):
    class Meta:
        widgets = {
        'password': forms.PasswordInput(),
    }
        model = User
        exclude = ['user_id','posts']

        
class UserUpdateForm(forms.ModelForm):


    class Meta:
        model = User

        fields = ['password', 'email','username', 'first_name', 'last_name']
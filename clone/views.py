from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from .forms import NewPostForm,ProfileUpdateForm
from .models import User,Post,Comment,Like
from django.core.checks import messages


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.all_posts ()
    return render(request,'index.html',{'posts':posts})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect(home)

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def profile(request):
    user = request.user

    return render(request, 'profile.html',{'user':user})



def logoutUser(request):
 logout(request)
 return redirect(home)
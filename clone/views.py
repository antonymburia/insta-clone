from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from .forms import NewPostForm,ProfileUpdateForm,CreateUserForm
from .models import Profile,Post,Comment,Like
from django.core.checks import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.all_posts()
    users = Profile.objects.all()
    return render(request,'index.html',{'posts':posts, 'users':users})

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        return redirect(home)

    else:
        form = CreateUserForm()
    
    return render(request,'registration/registration_form.html', {'form':form})

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
    user = request.Profile
    user = request.Profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            
            user.save()
        # return redirect(profile)
    else:
        form = ProfileUpdateForm()
    


    return render(request, 'profile.html',{'user':user,"form": form})



def logoutUser(request):
 logout(request)
 return redirect(home)
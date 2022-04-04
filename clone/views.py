from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from .forms import NewPostForm,ProfileUpdateForm
from .models import User,Post,Comment,Like
from django.core.checks import messages
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    posts = Post.all_posts()
    users = User.objects.all()
    return render(request,'index.html',{'posts':posts, 'users':users})

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
    user = request.user
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
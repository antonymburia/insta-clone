from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login
from .forms import NewPostForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'index.html')

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




def logoutUser(request):
 logout(request)
 return redirect(home)
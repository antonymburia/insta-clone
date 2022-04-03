from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'index.html')






def logoutUser(request):
 logout(request)
 return redirect(home)
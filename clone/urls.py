from django.urls import path 
from . import views

urlpatterns=[
   path('',views.home),
   path('logout/', views.logoutUser),
   path('new/post', views.new_post, name='new-post')
]
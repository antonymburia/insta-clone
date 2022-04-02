from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='articles/', blank=True)

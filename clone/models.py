from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to='articles/', blank=True)
    likes = models.ForeignKey('Like',on_delete = models.CASCADE,default=None)
    unlikes = models.ForeignKey('Unlike',on_delete = models.CASCADE,default=None)
    comments = models.ForeignKey('Comment', on_delete = models.CASCADE,default=None)


    def save_post(self):
     self.save()
             
    def delete_post(self):
     self.delete()
    
    @classmethod
    def all_posts(cls):
     '''
     get all posts
     
     '''
     posts=cls.objects.all()
     return posts

    @classmethod
    def get_one_post(cls):
     post=cls.objects.filter(id=id)
     return post

    @classmethod
    def search_post(cls,search_term):
     post = cls.objects.filter(name__icontains=search_term)
     return post

class Comment(models.Model):
 comment = models.CharField(max_length = 200)


 def save_comment(self):
  self.save()

 @classmethod
 def get_comments(cls):
  comments=cls.objects.all()
  return comments

class Like(models.Model):
 
 likes = models.IntegerField()

 def add_like(self):
  self.save()


  def __str__(self):
   return self.likes


class Unlike(models.Model):
 
 unlikes = models.IntegerField()

 def add_unlike(self):
  self.save()


  def __str__(self):
   return self.unlikes

    

    


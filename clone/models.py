from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField


class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    posts = models.ForeignKey('Post',on_delete=models.CASCADE,default=None)
    profile_pic = models.ImageField(upload_to='profile/', blank=True)

    @classmethod
    def get_users(cls):
        users=cls.objects.all()
        return users


    def __str__(self):
        return self.first_name

class Post(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = CloudinaryField('image')
    


    def save_post(self):
     self.save()
             
    def delete_post(self):
     self.delete()
    def __str__(self):
        return self.user
    
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
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE,default=None)
    comment = models.CharField(max_length = 200,  blank=True)


    def save_comment(self):
        self.save()

    @classmethod
    def get_comments(cls):
        comments=cls.objects.all()
        return comments

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default=None)
    likes = models.IntegerField(  blank=True)

    def add_like(self):
        self.save()


    def __str__(self):
        return self.likes


class Unlike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default=None)
    unlikes = models.IntegerField(blank=True)

    def add_unlike(self):
        self.save()


    def __str__(self):
        return self.unlikes

    

    


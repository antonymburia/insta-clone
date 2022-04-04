from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user_id = models.BigAutoField(primary_key=True,)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    username = models.CharField(max_length =30, blank=True)
    password = models.CharField(max_length=50, default=0000, blank=False)
    email = models.EmailField()
    posts = models.ForeignKey('Post',on_delete=models.CASCADE,default=None)
    profile_pic = CloudinaryField('image')
    bio = models.TextField()

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
    liked = models.ManyToManyField(User, default=None,blank= True,related_name='liked')
    author =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='author',blank= True,default=None)

 
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


    @property
    def like_count(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

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
    like_value = models.CharField(choices=LIKE_CHOICES,  default='Like', blank=True, max_length=20)

    def add_like(self):
        self.save()


    def __str__(self):
        return self.likes




    


from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    follower = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Followers')
    following =  models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Following')
    pass



class CommentResponse(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField()
    text = models.CharField(max_length=256)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField()
    text = models.CharField(max_length=256)
    responses = models.ForeignKey(CommentResponse, on_delete=models.CASCADE, related_name='respones')

class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.TextField(max_length=256)
    hashtags = models.TextField(max_length=64)
    likes = models.IntegerField(default=0)
    comments = models.ForeignKey(Comment, on_delete= models.CASCADE, related_name='comments_post', null = True, blank = True)
    date = models.DateField(auto_created=True)
    media = models.FileField(max_length=64, null=True, upload_to='media')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_post')

class Stories(models.Model):
    id = models.AutoField(primary_key=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments_story')
    date = models.DateField(auto_created=True)
    image = models.ImageField(max_length=64)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_story')



from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    follower = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Followers')
    following =  models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Following')
    pass





class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    caption = models.TextField(max_length=256)
    hashtags = models.TextField(max_length=64, null= True, blank=True)
    likes = models.IntegerField(default=0)
    date = models.DateField(auto_created=True)
    media = models.FileField(max_length=64, null=True, upload_to='media')
    titlepic = models.FileField(max_length=64, null=True, upload_to='title_pic')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_post')



class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField()
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE,  blank=True, null=True)

class CommentResponse(models.Model):
    id = models.AutoField(primary_key=True)
    likes = models.IntegerField()
    text = models.CharField(max_length=256)
    Comment = models.ForeignKey(Comment, default= 0, blank=True, on_delete=models.CASCADE, related_name='respones')
class Stories(models.Model):
    id = models.AutoField(primary_key=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments_story')
    date = models.DateField(auto_created=True)
    image = models.ImageField(max_length=64)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_story')



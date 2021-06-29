from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.

class Board(models.Model):
  name = models.CharField(null=1,max_length=50,unique=1)
  description = models.CharField(null=1,max_length=150)

  def __str__(self):
    return self.name

  def get_posts_count(self):
    return Post.objects.filter(topic__board=self).count()

  def get_last_post(self):
    return Post.objects.filter(topic__board=self).order_by('-created_dt').first()


class Topic(models.Model):
  subject = models.CharField(null=1,max_length=250)
  board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE) 
  created_by = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
  created_dt = models.DateTimeField(auto_now_add=1)
  views = models.PositiveIntegerField(default=0)

  def __str__(self):
    return self.subject

class Post(models.Model):
  message = models.TextField(max_length=5000)
  topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
  created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
  created_dt = models.DateTimeField(auto_now_add=1)    
  updated_by = models.ForeignKey(User, on_delete=models.CASCADE,null=1,related_name='+')
  updated_dt = models.DateTimeField(null=1)

  def __str__(self):
    truncated_message = Truncator(self.message)
    return truncated_message.chars(30)
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


STATUS_CHOICES = (
    (0, "Creating"),
    (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True, default='Category waiting for description')

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True, default='Post waiting for description')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='categories')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    likes_count = models.IntegerField(default=0)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True, default=None)
    saved_count = models.IntegerField(default=0)

    def __str__(self):
        return self.post_name


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    favorite = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_user')

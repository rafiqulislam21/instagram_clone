from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserPost(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    caption = models.CharField(max_length=400, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.caption)
        # return str(self.caption) + " | " + self.watchlist.title + " | " + str(self.review_user)

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    userpostC = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name="userpostC")
    
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
        # return str(self.caption) + " | " + self.watchlist.title + " | " + str(self.review_user)
        
class SaveUserPost(models.Model):
    save_user = models.ForeignKey(User, on_delete=models.CASCADE)
    userpostS = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name="userpostS")
    
    isSaved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} | {}".format(self.isSaved , self.created)
    

class LikeUserPost(models.Model):
    like_user = models.ForeignKey(User, on_delete=models.CASCADE)
    userpostL = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name="userpostL")
    
    isLiked = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{} | {}".format(self.isLiked , self.created)

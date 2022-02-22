from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserPost(models.Model):
    # review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    
    caption = models.CharField(max_length=400, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.caption)
        # return str(self.caption) + " | " + self.watchlist.title + " | " + str(self.review_user)

class Comment(models.Model):
    title = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
        # return str(self.caption) + " | " + self.watchlist.title + " | " + str(self.review_user)
        
class SaveUserPost(models.Model):
    isSaved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} | {}".format(self.isSaved , self.created)

from django.contrib import admin
from home_app.models import UserPost, SaveUserPost, Comment

# Register your models here.
admin.site.register(UserPost)
admin.site.register(Comment)
admin.site.register(SaveUserPost)
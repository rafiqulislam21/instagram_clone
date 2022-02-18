from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from home_app.api.views import (UserPostListView, UserPostCreateView, UserPostDetailView,
                                commentCreateView, commentListView, commentDetailView)

urlpatterns = [
    path('create/', UserPostCreateView.as_view(), name='feed-create'),
    path('list/', UserPostListView.as_view(), name='feed-list'),
    path('<int:pk>/', UserPostDetailView.as_view(),
         name='feed-detail'),  # including update, delete

    path('<int:pk>/comment-create/',
         commentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/comments/', commentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', commentDetailView.as_view(), name='comment-detail'),
]

# url example
# search: http://127.0.0.1:8000/home/feeds?search=nice
# update, delete http://127.0.0.1:8000/home/feeds/1/

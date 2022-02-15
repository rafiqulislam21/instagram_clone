from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from home_app.api.views import UserPostListView, UserPostCreateView, UserPostDetailView

urlpatterns = [
    path('feed-create/', UserPostCreateView.as_view(), name='feed-create'),
    path('feeds/', UserPostListView.as_view(), name='feed-list'),
    path('feeds/<int:pk>/', UserPostDetailView.as_view(), name='feed-detail'),
]

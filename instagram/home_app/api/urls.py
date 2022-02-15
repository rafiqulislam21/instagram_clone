from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from home_app.api.views import PostsListView

urlpatterns = [
    # path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('feeds/', PostsListView.as_view(), name='post-list'),
    # path('review/<int:pk>/', ReviewDetails.as_view(), name='review-detail'),
    
]

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters

# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from home_app.models import UserPost

from home_app.api.serializers import UserPostSerializer
from home_app.api.pagination import FeedCPagination, FeedPagination


# Create your views here.
class UserPostCreateView(generics.CreateAPIView):
    serializer_class = UserPostSerializer
    
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        
        UserPost.caption = serializer.validated_data['caption']
        UserPost.active = serializer.validated_data['active']
        
        serializer.save()


class UserPostListView(generics.ListAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
    
    #pagination
    pagination_class = FeedPagination
    
    #search filter
    filter_backends = [filters.SearchFilter]
    search_fields = ['caption']
    # search_fields = ['=title', 'platform__name']
    # url example: http://127.0.0.1:8000/home/feeds?search=nice


class UserPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer



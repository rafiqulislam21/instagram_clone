from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters

# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics

from home_app.models import UserPost, Comment, SaveUserPost

from home_app.api.serializers import UserPostSerializer, CommentSerializer, SaveUserPostSerializer
from home_app.api.pagination import FeedCPagination, FeedPagination


# Create your views here.
#==================user post====================================
class UserPostCreateView(generics.CreateAPIView):
    serializer_class = UserPostSerializer
    
    #permission only for logged in users
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        
        UserPost.caption = serializer.validated_data['caption']
        UserPost.active = serializer.validated_data['active']
        
        serializer.save()


class UserPostListView(generics.ListAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
    
    #permission only for logged in users
    permission_classes = [IsAuthenticated]
    
    #pagination
    pagination_class = FeedPagination
    
    #search filter
    filter_backends = [filters.SearchFilter]
    search_fields = ['caption']
    # search_fields = ['=title', 'platform__name']

#details generic class with default delete, update
class UserPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission only for logged in users
    permission_classes = [IsAuthenticated]
    
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer
#==================user post====================================


#=====================comments==================================
class commentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    
    #permission only for logged in users
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        
        Comment.caption = serializer.validated_data['title']
        Comment.active = serializer.validated_data['active']
        
        serializer.save()


class commentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    #permission only for logged in users
    permission_classes = [IsAuthenticated]
    
    #pagination
    pagination_class = FeedPagination

#details generic class with default delete, update
class commentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

#=====================comments==================================

#=====================save post==================================
class saveUserPostView(generics.CreateAPIView):
    serializer_class = SaveUserPostSerializer

    #permission only for logged in users
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):

        SaveUserPost.isSaved = serializer.validated_data['isSaved']
        
        serializer.save()
        
class unsaveUserPostView(generics.DestroyAPIView):
    queryset = SaveUserPost.objects.all()
    serializer_class = SaveUserPostSerializer
    
    #permission only for logged in users
    permission_classes = [IsAuthenticated]

#=====================save post==================================

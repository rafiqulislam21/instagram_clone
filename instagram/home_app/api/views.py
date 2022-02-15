from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from home_app.models import UserPost

from home_app.api.serializers import UserPostSerializer


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


class UserPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserPost.objects.all()
    serializer_class = UserPostSerializer



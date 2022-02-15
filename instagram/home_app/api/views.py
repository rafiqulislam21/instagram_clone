from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from home_app.models import Posts

from home_app.api.serializers import PostsSerializer


# Create your views here.

# class ReviewCreate(generics.CreateAPIView):
#     # queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     #custom throttling, restriction of request(option 1----)
#     throttle_classes = [ReviewCreateThrottle, AnonRateThrottle]
    
#     def get_queryset(self):
#         return Review.objects.all()

#     def perform_create(self, serializer):
#         pk = self.kwargs.get('pk')
#         watchlist = WatchList.objects.get(pk=pk)
        
#         review_user = self.request.user
#         review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
#         if review_queryset.exists():
#             raise ValidationError("Already reviewed this movie!")
        
#         if watchlist.number_rating == 0:
#             watchlist.avg_rating = serializer.validated_data['rating']
#         else:
#             watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
#         watchlist.number_rating += 1
#         watchlist.save()
        
#         serializer.save(watchlist=watchlist, review_user=review_user)


class PostsListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


# class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # permission_classes = [IsAuthenticatedOrReadOnly] #permission_classes
#     permission_classes = [IsReviewUserOrReadOnly] #custom permisson
    
#     #custom throttling, restriction of request(option 2----)
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'review-details'



from rest_framework import serializers
from home_app.models import UserPost

# model based serializers----------------   
class UserPostSerializer(serializers.ModelSerializer):
    # adding custom field without model serial
    # len_name = serializers.SerializerMethodField()
    
    # nested serializers/ one to many serializers
    # reviews = ReviewSerializer(many=True, read_only=True)
    
    # overrides the foreign key to another field
    # platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = UserPost
        fields = "__all__"
    
    # field level validation
    def validate_caption(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Caption is too short")
        return value      


# class ReviewSerializer(serializers.ModelSerializer):
#     review_user = serializers.StringRelatedField(read_only=True)
    
#     class Meta:
#         model = Review
#         # fields = "__all__"
#         exclude = ("watchlist",)
 
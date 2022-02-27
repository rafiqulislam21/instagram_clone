from rest_framework import serializers
from home_app.models import UserPost, Comment, SaveUserPost

# model based serializers----------------


class UserPostSerializer(serializers.ModelSerializer):
    # adding custom field without model serial
    # len_name = serializers.SerializerMethodField()

    # nested serializers/ one to many serializers
    comments = CommentSerializer(many=True, read_only=True)

    # overrides the foreign key to another field
    # platform = serializers.CharField(source='platform.name')
    post_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = UserPost
        fields = "__all__"

    # field level validation
    def validate_caption(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Caption is too short")
        return value


class CommentSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        # exclude = ("watchlist",)
    # field level validation

    def validate_title(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Comment shouldn't empty")
        return value


class SaveUserPostSerializer(serializers.ModelSerializer):
    save_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = SaveUserPost
        fields = "__all__"
        
    # field level validation
    def validate_title(self, value):
        if isSaved != True or isSaved != False:
            raise serializers.ValidationError("isSaved should be True or False")
        return value
 
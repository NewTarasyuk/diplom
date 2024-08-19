from rest_framework import serializers
from posts.models import Post, PostImage, Like, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = 'ttvv'
        fields = ['id', 'user', 'post', 'text', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'ghgvcx'
        fields = ['id','post','image']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'post']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        if Like.objects.filter(user=validated_data['user'], post=validated_data['post']).exists():
            raise serializers.ValidationError('You have already liked this post')

        return super().create(validated_data)

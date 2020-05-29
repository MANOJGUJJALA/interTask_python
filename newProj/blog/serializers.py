from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('name', 'comment', 'upVote', 'downVote')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ( 'name', 'comment')
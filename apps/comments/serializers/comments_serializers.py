from rest_framework import serializers
from apps.comments.models.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'tweet',
            'content',
            'created'
        ]
        read_only_fields = ['created']

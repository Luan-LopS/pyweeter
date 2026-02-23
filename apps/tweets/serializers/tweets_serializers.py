from rest_framework import serializers
from apps.tweets.models.models import Tweet
from apps.users.serializers.user_serializer import UserSerializer


class TweetsSerializers(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, public=True)
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'id',
            'user',
            'content',
            'created',
            'liked',
            'likes_count',
            'comment'
        ]

        extra_kwargs = {
            'user': {'read_only': True}
        }

    def get_liked(self, obj):
        request = self.context.get('request')
        if not request or request.user.is_anonymous:
            return False

        return obj.likes.filter(user=request.user).exists()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comment(self, obj):
        return [
            {
                'id': c.id,
                'user': c.user.username,
                'content': c.content,
                'created': c.created
            }
            for c in obj.comments.all()
        ]

from rest_framework.serializers import ModelSerializer
from apps.likes.models.models import Like


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'id',
            'user',
            'tweet',
            'created',
        ]
        read_only_fields = [
            'user',
            'created'
        ]

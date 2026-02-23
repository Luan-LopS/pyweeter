from rest_framework import serializers
from apps.followers.models.models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    follower_name = serializers.SerializerMethodField()
    following_name = serializers.SerializerMethodField()

    class Meta:
        model = Follower
        fields = (
            'id',
            'following',
            'following_username',
            'follower',
            'follower_username',
            'created',
        )
        read_only_fields = ('created',)

    def get_follower_name(self, obj):
        return obj.follower.get_full_name() or obj.follower.username

    def get_following_name(self, obj):
        return obj.following.get_full_name() or obj.following.username
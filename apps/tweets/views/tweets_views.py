from rest_framework.viewsets import ModelViewSet
from apps.followers.models.models import Follower
from apps.tweets.models.models import Tweet
from apps.tweets.serializers.tweets_serializers import TweetsSerializers
from rest_framework.permissions import IsAuthenticated


class TweetViewSet(ModelViewSet):
    serializer_class = TweetsSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_ids = Follower.objects.filter(user=user).values_list(
            'following_id',
            flat=True
            )
        return Tweet.objects.filter(user_id__in=list(following_ids)+[user.id]
                                    ).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer

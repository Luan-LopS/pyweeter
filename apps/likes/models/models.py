from django.db import models
from apps.tweets.models.models import Tweet
from apps.users.models.models import User


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
        )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        related_name='likes'
        )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tweet')

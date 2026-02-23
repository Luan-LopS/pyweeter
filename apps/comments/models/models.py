from django.db import models
from apps.tweets.models.models import Tweet
from apps.users.models.models import User


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(
        max_length=285,
        blank=False,
        null=False
    )
    created = models.DateTimeField(auto_now_add=True)

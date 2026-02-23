from django.db import models
from django.conf import settings


class Follower(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followers'
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followings'
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'following')

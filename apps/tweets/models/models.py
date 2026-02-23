from django.db import models
from apps.users.models.models import User


class Tweet(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tweets'
        )
    content = models.TextField(max_length=280, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

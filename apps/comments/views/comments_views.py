from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.comments.serializers.comments_serializers import CommentSerializer
from apps.comments.models.models import Comment
from rest_framework.exceptions import ValidationError


class CommentsViews(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        tweet_id = self.request.query_params.get('tweet')
        if tweet_id:
            return self.queryset.filter(tweet_id=tweet_id)
        return self.queryset

    def perform_create(self, serializer):
        tweet_id = self.request.data.get('tweet')

        if not tweet_id:
            raise ValidationError({'tweet': 'This field is required.'})
        serializer.save(
            user=self.request.user,
            tweet_id=tweet_id
        )

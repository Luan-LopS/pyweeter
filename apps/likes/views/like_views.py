from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.tweets.models.models import Tweet
from apps.likes.serializers.like_serializers import LikeSerializer
from apps.likes.models.models import Like


class LikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post', 'delete'])
    def like(self, request, pk=None, **kwargs):
        try:
            tweet = Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            return Response(
                {'error': 'Tweet não encontrado'},
                status=status.HTTP_404_NOT_FOUND
                )

        user = request.user

        if request.method == 'POST':
            _, created = Like.objects.get_or_create(user=user, tweet=tweet)
            if created:
                return Response(
                    {'liked': True},
                    status=status.HTTP_200_OK
                    )
            return Response(
                {'liked': True},
                status=status.HTTP_200_OK
                )
        elif request.method == 'DELETE':
            deleted_count, _ = Like.objects.filter(
                user=user,
                tweet=tweet).delete()
            if deleted_count > 0:
                return Response(
                    {'liked': False},
                    status=status.HTTP_201_CREATED
                    )
            return Response(
                {'liked': False},
                status=status.HTTP_200_OK
                )

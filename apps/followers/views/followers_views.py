from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.followers.models.models import Follower
from apps.followers.serializers.followers_serializers import FollowerSerializer
from apps.users.models.models import User
from apps.users.serializers.user_serializer import UserSerializer
from django.db.models import Q


class FollowersViews(ModelViewSet):
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Follower.objects.filter(
            user=self.request.user
        ).order_by('-created')

    @action(detail=False, methods=['get'])
    def relations(self, request, *args, **kwargs):
        user = request.user

        following = User.objects.filter(
            followings__user=user
        )

        followers = User.objects.filter(
            followers__following=user
        )

        return Response({
            'following': UserSerializer(
                following, many=True, public=True,
                context={'request': request}).data,
            'followers': UserSerializer(followers, many=True, public=True,
                                        context={'request': request}).data
        })

    @action(detail=False, methods=['get'],
            url_path='not_followed')
    def not_followed(self, request, *args, **kwargs):
        user = request.user

        following_ids = Follower.objects.filter(user=user).values_list(
            'following_id', flat=True)

        users_id = User.objects.exclude(
            Q(id__in=following_ids) | Q(id=user.id)
        )

        return Response(UserSerializer(
            users_id, many=True, public=True,
            context={'request': request}).data)

    @action(detail=False, methods=['post', 'delete'],
            url_path=r'(?P<user_id>[^/.]+)/follow')
    def follower(self, request, user_id=None, *args, **kwargs):
        try:
            following_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {'error': 'User não encontrado'},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'POST':
            _, created = Follower.objects.get_or_create(
                user=request.user,
                following=following_user
            )

            if created:
                return Response(
                    {'followings': True},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {'followings': True},
                    status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            Follower.objects.filter(
                user=request.user,
                following=following_user
            ).delete()
            return Response(
                {'followings': False},
                status=status.HTTP_200_OK
                )

from rest_framework import mixins, viewsets
from apps.users.models.models import User
from apps.users.serializers.user_serializer import UserSerializer
from rest_framework.permissions import AllowAny,  IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action in ['update', 'partial_update']:
            return User.objects.filter(id=self.request.user.id)
        elif self.action == 'list':
            return User.objects.exclude(id=self.request.user.id)
        return User.objects.none()

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request, *args, **kwargs):
        user = request.user

        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data)

        elif request.method == 'PATCH':
            serializer = self.get_serializer(
                user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = self.get_serializer(
            users, many=True,
            context={'request': request})
        return Response(serializer.data)

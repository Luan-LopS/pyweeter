from rest_framework import serializers
from apps.users.models.models import User
from apps.followers.models.models import Follower


class UserSerializer(serializers.ModelSerializer):
    is_following = serializers.BooleanField(read_only=True)
    follows_me = serializers.BooleanField(read_only=True)
    profile_picture = serializers.ImageField(
        max_length=None, use_url=True, required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'email',
            'bio',
            'profile_picture',
            'password',
            'is_following',
            'follows_me'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': True, 'min_length': 8},
            'username': {'required': True, 'min_length': 8},
            'email': {'required': True},
            'password': {'write_only': True, 'min_length': 8, 'required': True}
        }

    def __init__(self, *args, **kwargs):
        public = kwargs.pop('public', False)
        super().__init__(*args, **kwargs)
        if public:
            allowed_fields = {
                'id',
                'name',
                'username',
                'bio',
                'profile_picture',
                'is_following',
                'follows_me'
            }
            for field in list(self.fields):
                if field not in allowed_fields:
                    self.fields.pop(field)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get(
            'request') if isinstance(self.context, dict) else None
        request_user = getattr(request, 'user', None)

        if instance.profile_picture and request:
            data['profile_picture'] = request.build_absolute_uri(
                instance.profile_picture.url)

        if getattr(request_user, 'is_authenticated', False):
            data['is_following'] = Follower.objects.filter(
                user=request_user, following=instance
            ).exists()
            data['follows_me'] = Follower.objects.filter(
                user=instance, following=request_user
            ).exists()
        else:
            data['is_following'] = False
            data['follows_me'] = False
        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        if not password or len(password) < 8:
            raise serializers.ValidationError(
                {'password': 'Senha obrigatória e mínimo 8 caracteres'})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        profile_picture = validated_data.pop('profile_picture', None)
        name = validated_data.pop('name', None)
        bio = validated_data.pop('bio', None)

        if password:
            if len(password) < 8:
                raise serializers.ValidationError(
                    {'password': 'Tamanho mínimo 8 caracteres'})
            instance.set_password(password)

        if profile_picture is not None:
            instance.profile_picture = profile_picture
        if name is not None:
            instance.name = name
        if bio is not None:
            instance.bio = bio

        instance.save()
        return instance

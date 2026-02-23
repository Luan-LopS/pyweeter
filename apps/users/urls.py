from django.urls import path, include
from rest_framework import routers
from apps.users.views.user_views import UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]

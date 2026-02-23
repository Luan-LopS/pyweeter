from django.urls import path, include
from rest_framework import routers
from apps.followers.views.followers_views import FollowersViews

router = routers.SimpleRouter()
router.register(r'followers',  FollowersViews, basename='followers')

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import path, include
from rest_framework import routers
from apps.likes.views.like_views import LikeView

router = routers.SimpleRouter()
router.register(r'likes',  LikeView, basename='like')

urlpatterns = [
    path('', include(router.urls))
]

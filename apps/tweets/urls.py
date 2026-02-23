from django.urls import path, include
from rest_framework import routers
from apps.tweets.views.tweets_views import TweetViewSet

router = routers.SimpleRouter()
router.register(r'tweets',  TweetViewSet, basename='tweets')

urlpatterns = [
    path('', include(router.urls))
]

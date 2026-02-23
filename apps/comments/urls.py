from django.urls import path, include
from rest_framework import routers
from apps.comments.views.comments_views import CommentsViews

router = routers.SimpleRouter()
router.register(r'comments', CommentsViews, basename='comments')

urlpatterns = [
    path('', include(router.urls))
]

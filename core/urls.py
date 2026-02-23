from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, re_path, include
from core import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'^api/(?P<version>v1|v2)/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
        ),
    re_path(
        r'^api/(?P<version>v1|v2)/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
        ),
    re_path(r'^api/(?P<version>v1|v2)/', include([
        path('',  include('apps.users.urls')),
        path('', include('apps.tweets.urls')),
        path('', include('apps.likes.urls')),
        path('', include('apps.followers.urls')),
        path('', include('apps.comments.urls'))
        ])
    )
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

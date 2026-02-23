from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('tweets/', include('apps.tweets.url')),
    path('', include('apps.tweets.url')),

]

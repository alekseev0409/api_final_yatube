from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    CommentViewSet,
    GroupViewSet,
    PostViewSet,
    FollowViewSet
)


router = DefaultRouter()
router.register(
    'v1/posts',
    PostViewSet,
    basename='Post'
)
router.register(
    'v1/groups',
    GroupViewSet,
    basename='Group'
)
router.register(
    r'v1/posts/(?P<id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment'
)


router.register(
    r'v1/follow',
    FollowViewSet,
    basename='Follow'
)


urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]

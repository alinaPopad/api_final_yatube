from rest_framework import routers
from django.urls import path, include

from .views import GroupViewSet, FollowViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()

router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('posts', PostViewSet, basename='posts')
router.register(r'follow', FollowViewSet, basename='follows')

router.register(r'groups', GroupViewSet, basename='groups')


urlpatterns = [
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path('v1/', include(router.urls)),
]

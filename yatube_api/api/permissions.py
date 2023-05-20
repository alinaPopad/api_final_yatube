from rest_framework import permissions
from rest_framework.permissions import BasePermission
from posts.models import Follow


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            obj.author == request.user
            or (request.method == 'POST' and request.user.is_authenticated)
        )


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.is_author(request, obj)

    def is_author(self, request, obj):
        return obj.author == request.user


class IsNotAlreadyFollowing(permissions.BasePermission):
    message = 'You are already following this user.'

    def has_permission(self, request, view):
        following = request.data.get('following')
        user = request.user
        if following and Follow.objects.filter(
                user=user,
                following=following
        ).exists():
            return False
        return True

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from posts.models import Post, Group
from .serializers import PostSerializer, GroupSerializer
from .serializers import FollowSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def peform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.follower.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets

from .custom_mixins import CreateListViewSet
from posts.models import Comment, Follow, Group, Post, User
from .pagination import PostPagination
from .permissions import AuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer,
                          GroupSerializer, PostSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
    filter_backends = (filters.OrderingFilter,)
    pagination_class = PostPagination
    ordering = ('id',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]
    filter_backends = (filters.OrderingFilter,)
    ordering = ('id',)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if not self.kwargs.get('pk'):
            return Comment.objects.filter(post=post_id)
        comment_id = self.kwargs.get('pk')
        return Comment.objects.filter(id=comment_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(
            author=self.request.user,
            post=post
        )


class FollowViewSet(CreateListViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['=following__username']

    def get_queryset(self):
        if not self.request.query_params.get('search'):
            user = User.objects.get(username=self.request.user.username)
            return user.follower
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import viewsets

from django.shortcuts import render
from blog.models import Post
from blog.models import Comment
from blog.serializers import PostSerializers
from blog.serializers import CommentSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

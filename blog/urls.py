from django.urls import path
from blog.views import PostViewSet
from blog.views import CommentViewSet

urlpatterns = [
    path('post', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comment', CommentViewSet.as_view({'get':'list', 'post':'create'})),
]

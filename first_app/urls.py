from django.urls import path
from first_app.views import UserViewSet

urlpatterns = [
    path('<uuid:uuid>/',
         UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='users'),
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='users'),
]

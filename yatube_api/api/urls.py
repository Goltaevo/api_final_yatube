from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('v1/groups', GroupViewSet, basename='groups')
router_v1.register('v1/posts', PostViewSet, basename='posts')
router_v1.register('v1/follow', FollowViewSet, basename='follow')

router_v1.register(
    r'v1/posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),
]

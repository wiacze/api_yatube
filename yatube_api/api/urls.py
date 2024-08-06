from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = DefaultRouter()

router.register('groups', GroupViewSet, 'groups')
router.register('posts', PostViewSet, 'posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]

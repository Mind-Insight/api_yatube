from django.urls import path, include

from rest_framework.authtoken import views
from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
router.register(r"posts", PostViewSet, basename="post")
router.register(r"groups", GroupViewSet, basename="group")


urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
]

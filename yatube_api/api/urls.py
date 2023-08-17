from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
router_v1.register("posts", PostViewSet, basename="post")
router_v1.register("groups", GroupViewSet, basename="group")


urlpatterns = [
    path("v1/api-token-auth/", views.obtain_auth_token),
    path("v1/", include(router_v1.urls)),
]

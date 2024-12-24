from rest_framework import routers
from core.post.models import Post
from core.post.viewsets import PostViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### POST ###################### #
# ##################################################################### #

router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
]
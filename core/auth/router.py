from rest_framework import routers
from core.user.models import User
from core.auth.viewsets import RegisterViewset, LoginViewSet, RefreshViewSet


router = routers.SimpleRouter()

# ##################################################################### #
# ################### AUTH ###################### #
# ##################################################################### #

router.register(r'auth/register', RegisterViewset, basename='auth-register')
router.register(r'auth/login', LoginViewSet,basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

urlpatterns = [
    *router.urls,
]
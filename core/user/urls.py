from django.urls import path, include
from .router import router
from rest_framework.routers import DefaultRouter
from core.user.viewset import UserViewSet


urlpatterns = [
    path('', include(router.urls)),
]

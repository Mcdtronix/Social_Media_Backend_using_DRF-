from django.urls import path, include
from .router import router
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', include(router.urls)),
]

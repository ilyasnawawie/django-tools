from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminAuthTokenViewSet

router = DefaultRouter()
router.register(r'admin_auth_tokens', AdminAuthTokenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

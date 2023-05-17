from rest_framework import viewsets
from .models import AdminAuthToken
from .serializers import AdminAuthTokenSerializer

class AdminAuthTokenViewSet(viewsets.ModelViewSet):
    queryset = AdminAuthToken.objects.all()
    serializer_class = AdminAuthTokenSerializer

from rest_framework import serializers
from .models import AdminAuthToken

class AdminAuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAuthToken
        fields = '__all__'

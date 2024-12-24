from rest_framework import serializers
from core.user.models import User
from core.abstract.serializers import AbstractSerializer


class UserSerializers(AbstractSerializer):

    
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email', 'is_active','created', 'updated']
        read_only_fields = ['is_active']
        
        
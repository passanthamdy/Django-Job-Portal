from accounts.models import User
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('company_name', 'address', 'history', 'allow_notification', 'user_type')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('allow_notification')

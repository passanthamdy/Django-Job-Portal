from rest_framework import serializers
from accounts.models import User
from tags.serializers import TagSerializer


class DeveloperViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'tags', 'cv', 'gender']


class UsersHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

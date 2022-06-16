from rest_framework import serializers
from accounts.models import User
from tags.serializers import TagSerializer


class DeveloperViewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'

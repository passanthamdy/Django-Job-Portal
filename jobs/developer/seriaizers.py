from rest_framework import serializers
from jobs.models import Job
from accounts.models import User
from tags.models import Tag


class JobOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'username', 'address']
        model = User


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Tag


class DeveloperJobsSerializer(serializers.ModelSerializer):

    job_owner = JobOwnerSerializer()
    Tags = TagsSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Job
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = User


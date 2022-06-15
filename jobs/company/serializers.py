from rest_framework import serializers
from ..models import Job
from accounts.models import User
from tags.models import Tag

"""
tagserializer and user serializer are user for testing purpose only
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','gender']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','name']

class JobSerializer(serializers.ModelSerializer):
    job_owner=UserSerializer(many=False,read_only=True)
    applied_developers=UserSerializer(many=True)
    developer=UserSerializer(many=False)
    Tags=TagSerializer(many=True)
    class Meta:
        model=Job
        fields=['id','name','job_owner','Tags','applied_developers',
        'developer','description','status','creation_time','modification_time',]
        optional_fields=['applied_developers','developer','status']

class JobCreateSerializer(serializers.ModelSerializer):
    user=User.objects.get(id=5)
    job_owner= serializers.HiddenField(
        default=user,
    )
    class Meta:
        model=Job
        fields=['id','name','Tags','applied_developers',
        'developer','description','creation_time','modification_time','job_owner']
        optional_fields=['applied_developers','developer',]

    # def create(self, validated_data):
    #      jobs = Job.objects.create( **validated_data)
    #      tags = validated_data.pop('tags_id')

    #      for tg in tags:
    #         jobs.tags.add(tg)
    #      return jobs


class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model =Job
        fields =['name','Tags','description','status']
        optional_fields=['name','Tags','description','status']
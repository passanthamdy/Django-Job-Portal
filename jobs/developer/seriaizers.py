from rest_framework import serializers
from jobs.models import Job
from accounts.models import User
from tags.models import Tag
from accounts.api.v1.serializers import CompanySerializer, DeveloperSerializer


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name']
        model = Tag

class DeveloperJobsSerializer(serializers.ModelSerializer):
    job_owner = CompanySerializer()
    applied_developers = DeveloperSerializer(many=True)
    developer = DeveloperSerializer(many=False)
    Tags = TagsSerializer(many=True)

    class Meta:
        model = Job
        fields = ['id', 'name', 'job_owner', 'Tags', 'applied_developers',
                  'developer', 'description', 'status', 'creation_time', 'modification_time', ]
        #optional_fields = ['applied_developers', 'developer', 'status']





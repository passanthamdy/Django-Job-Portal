from functools import partial
from inspect import stack
from django.shortcuts import render
from requests import request
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import JobSerializer, JobUpdateSerializer, JobCreateSerializer
from jobs.models import Job
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view


# class ListCompanyJobs(generics.ListAPIView):
#     #self.request.user
#     user=User.objects.get(id=5)
#     queryset=Job.objects.filter(job_owner=user)
#     serializer_class=JobSerializer
class ListCompanyJobs(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all jobs related to the requested user.
        """
        user = User.objects.get(id=5)
        jobs = Job.objects.filter(job_owner=user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create new job with 
        """

        serializer = JobCreateSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            print("is valid")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteCompanyJob(APIView):
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobUpdateSerializer(job, data=request.data, partial=True)
        if serializer.is_valid():
            if job.status == "OPEN":
                serializer.save()
                return Response(serializer.data)
        return Response({"details": "your job cannot be edited "}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        st = status.HTTP_400_BAD_REQUEST
        if job.status == 'OPEN':
            print('got delete')
            st = status.HTTP_204_NO_CONTENT
            job.delete()
            return Response({"details": "your job is deleted"}, status=st)


@api_view(['POST'])
def AcceptDeveloper(request, pk):
    st = status.HTTP_400_BAD_REQUEST
    job = Job.objects.get(pk=pk)
    id = request.data['id']
    user = User.objects.get(id=id)
    if job.status == 'OPEN' and job.developer is None:
        job.developer=user
        job.save()
        return Response({"details": "Developer has been accepted"}, status=status.HTTP_201_CREATED)
    return Response({"details": "Developer can't be accepted"}, status=status.HTTP_201_CREATED)

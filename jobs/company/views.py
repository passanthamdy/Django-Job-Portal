from rest_framework.views import APIView
from .serializers import JobSerializer, JobUpdateSerializer, JobCreateSerializer
from jobs.models import Job
from accounts.models import User
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view


class ListCompanyJobs(APIView):
   
    def get(self, request, format=None):
        """
        Return a list of all jobs related to the requested user.
        """
        
        jobs = Job.objects.filter(job_owner=request.user)
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
    """
    get the job object 
    """
    def get_object(self, pk):
        try:
            return Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404
    """
    retrieve one job
    """
    def get(self, request, pk, format=None):
        print(request.user)
        job = self.get_object(pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
    """
    Update job only if it's open and has permission to update it as a job owner 
    """
    def put(self, request, pk, format=None):
        
        job = self.get_object(pk)
        if request.user == job.job_owner:
            serializer = JobUpdateSerializer(job, data=request.data, partial=True)
            if serializer.is_valid():
                if job.status == "OPEN":
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response({"details": "You don't have the persmission to edit or delete this job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "your job cannot be edited "}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        st = status.HTTP_400_BAD_REQUEST
        if request.user == job.job_owner:
            if job.status == 'OPEN':
                print('got delete')
                st = status.HTTP_204_NO_CONTENT
                job.delete()
                return Response({"details": "your job is deleted"}, status=st)
        else:
            return Response({"details": "You don't have the persmission to edit or delete this job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "job is not deleted"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def AcceptDeveloper(request, pk):
    st = status.HTTP_400_BAD_REQUEST
    job = Job.objects.get(pk=pk)
    id = request.data['id']
    user = User.objects.get(id=id)
    if job.status == 'OPEN' and job.developer is None:
        if user in job.applied_developers.all():
            user.in_job = True
            job.developer = user
            job.save()
            user.save()
        else:
            return  Response({"details": "this developer didn't apply for your job"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"details": "Developer has been accepted"}, status=status.HTTP_201_CREATED)
    return Response({"details": "Developer can't be accepted"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def mark_finish(request,pk):
    job = Job.objects.get(id=pk)
    id=job.developer.id
    user=User.objects.get(id=id)
    if job.job_owner == request.user:
        job.status = 'FINISHD'
        user.in_job=False
        user.save()
        job.save()
        return Response({"details":f"Your job is Finished"},status=status.HTTP_201_CREATED)


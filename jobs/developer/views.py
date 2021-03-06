from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404

from accounts.models import User
from jobs.models import Job
from .seriaizers import DeveloperJobsSerializer


@api_view(["GET"])
def jobs_list_for_developer(request):
    jobs_list = Job.objects.filter(status="OPEN")
    serializer = DeveloperJobsSerializer(jobs_list, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def job_details(request, job_id):
    job_detail = Job.objects.get(pk=job_id)
    serializer = DeveloperJobsSerializer(job_detail)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def apply_for_job(request, job_id):
    user = request.user
    job = Job.objects.get(pk=job_id)
    print( job.status)
    if job.status == 'OPEN' and user.in_job == False:
        print('valid')
        job.applied_developers.add(user)
        job.save()
        return Response({"details": f"{user.username}Developer Applied succesfully"}, status=status.HTTP_201_CREATED)
    return Response({"details": "You can't apply for this job"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def mark_finish(request,job_id):
    job = Job.objects.get(pk=job_id)
    if job.developer == request.user:
        job.status = 'FINISHD'
        user=User.objects.get(id=request.user.id)
        user.in_job= False 
        user.save()
        job.save()
        return Response({"details":f"Your job is Finished"},status=status.HTTP_201_CREATED)


@api_view(["GET"])
def current_job(request):
        try:
            job_detail= Job.objects.get(developer=request.user)
            print("here prinnnt",request.user)
        except Job.DoesNotExist:
            raise Http404('No Current Job')
        serializer = DeveloperJobsSerializer(job_detail)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


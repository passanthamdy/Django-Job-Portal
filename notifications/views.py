from django.shortcuts import render
from rest_framework.views import APIView
from .models import Notification

class ListNotifications(APIView):
   
    def get(self, request, format=None):
        """
        Return a list of all notifications related to the requested user.
        """
        
        jobs = Notification.objects.filter(user=request.user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


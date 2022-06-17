from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from .serializers import DeveloperViewSerializer
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from profiles.permissions import UserWritePermission
from rest_framework.generics import UpdateAPIView

# from .permissions import MyPermission

@api_view(["GET"])
def profile_view(request, developer_id):
    developer_instance = User.objects.filter(pk=developer_id).first()
    serializer = DeveloperViewSerializer(developer_instance)
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    if developer_instance.user_type == 'DEVELOPER':
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = "this url is to get developer profile !"

    return Response(**response)



class UpdataProfile(UpdateAPIView):

    queryset=User.objects.all()
    serializer_class=DeveloperViewSerializer
    permission_classes=[UserWritePermission]



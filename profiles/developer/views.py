from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from .serializers import DeveloperViewSerializer
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


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


@api_view(['PUT', 'PATCH'])
def profile_update(request, developer_id):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}
    developer_instance = User.objects.filter(pk=developer_id).first()
    serializer = DeveloperViewSerializer(instance=developer_instance, data=request.data)
    if request.method == 'PUT':
        serializer = DeveloperViewSerializer(instance=developer_instance, data=request.data)
    else:
        serializer = DeveloperViewSerializer(instance=developer_instance, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED
    else:
        response['data'] = serializer.errors

    return Response(**response)



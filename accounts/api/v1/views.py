from django.contrib.auth import logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .serializers import DeveloperSerializer, CompanySerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes


@api_view(['POST'])
@permission_classes([])
def developer_signup(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}

    serializer = DeveloperSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED

    else:
        response['data'] = serializer.errors

    return Response(**response)


@api_view(['POST'])
@permission_classes([])
def company_signup(request):
    response = {'data': None, 'status': status.HTTP_400_BAD_REQUEST}

    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response['data'] = serializer.data
        response['status'] = status.HTTP_201_CREATED

    else:
        response['data'] = serializer.errors

    return Response(**response)


@api_view(["GET"])
def user_logout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')

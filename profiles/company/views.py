from accounts.models import User
from django.core.exceptions import ObjectDoesNotExist
from profiles.permissions import UserWritePermission
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profiles.developer.serializers import UsersHistorySerializer
from .serializers import CompanySerializer, NotificationSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.generics import UpdateAPIView


# get company by id
@api_view(["GET"])
def get_company(request, company_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        company = User.objects.get(id=company_id)
        serializer = CompanySerializer(company, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'object does not exit'}
        response['status'] = status.HTTP_204_NO_CONTENT
    finally:
        return Response(**response)


class UpdataProfile(UpdateAPIView):
    queryset=User.objects.all()
    serializer_class=CompanySerializer
    permission_classes=[UserWritePermission]


# toggle
@api_view(["PATCH"])
def allow_notification(request, company_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        company = User.objects.get(id=company_id)
        serializer = NotificationSerializer(company, many=False)
        response['data'] = serializer.data
        response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'object does not exit'}
        response['status'] = status.HTTP_204_NO_CONTENT
    finally:
        return Response(**response)


@api_view(['GET'])
def get_history(request, id):
    user = User.objects.get(id=id)
    users = user.history.all()
    serializer = UsersHistorySerializer(users, many=True)
    return Response(data=serializer.data)

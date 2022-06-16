from accounts.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profiles.developer.serializers import  UsersHistorySerializer
from .serializers import CompanySerializer, NotificationSerializer


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


# update company details
@api_view(["PUT", "PATCH"])
def update_company(request, company_id):
    response = {'data': {}, 'status': status.HTTP_404_NOT_FOUND}
    try:
        company = User.objects.get(id=company_id)
        # edit logic
        if request.method == 'PUT':
            serializer = CompanySerializer(instance=company, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                response['data'] = serializer.data
                response['status'] = status.HTTP_200_OK
        elif request.method == 'PATCH':
            serializer = CompanySerializer(company, data=request.data, )
            if serializer.is_valid(raise_exception=True):
                print(request.data)
                serializer.save()
                response['data'] = serializer.data
                response['status'] = status.HTTP_200_OK
    except ObjectDoesNotExist:
        response['data'] = {'object does not exit'}
        response['status'] = status.HTTP_204_NO_CONTENT
    finally:
        return Response(**response)


# get company by id
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
    user=User.objects.get(id=id)
    users=user.history.all()
    serializer=UsersHistorySerializer(users, many=True)
    return Response(data=serializer.data)

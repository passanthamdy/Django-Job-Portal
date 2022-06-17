import imp
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import TagSerializer
from .models import Tag

# Create your views here.
class ListCreateTag(ListCreateAPIView):
    queryset=Tag.objects.all()
    serializer_class=TagSerializer


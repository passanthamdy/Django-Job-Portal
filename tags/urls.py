from django.urls import path
from . import views

app_name = 'tags'
urlpatterns = [
    path('list/', views.ListCreateTag.as_view(), name='tag-list'),
   
]

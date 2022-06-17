from django.urls import path
from .views import profile_view, UpdataProfile

app_name = 'developer_profile'
urlpatterns = [
    path('update/<int:pk>', UpdataProfile.as_view(), name='ho-drf'),
    path('view/<int:developer_id>', profile_view, name='list'),


]
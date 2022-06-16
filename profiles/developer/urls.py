from django.urls import path
from .views import profile_view, profile_update

app_name = 'developer_profile'
urlpatterns = [
    path('update/<int:developer_id>', profile_update, name='ho-drf'),
    path('view/<int:developer_id>', profile_view, name='list'),


]
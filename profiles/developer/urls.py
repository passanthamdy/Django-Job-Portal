from django.urls import path
from .views import profile_view, UpdataProfile, allow_notification

app_name = 'developer_profile'
urlpatterns = [
    path('dev/<int:developer_id>/details/', profile_view, name='list'),
    path('dev/<int:pk>/update/', UpdataProfile.as_view(), name='ho-drf'),
    path('dev/<int:developer_id>/allow_notification/', allow_notification),

]

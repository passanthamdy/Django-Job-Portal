from django.urls import path
from .views import profile_view, UpdataProfile, allow_notification

app_name = 'developer_profile'
urlpatterns = [
    path('update/<int:pk>', UpdataProfile.as_view(), name='ho-drf'),
    path('view/<int:developer_id>', profile_view, name='list'),
    path('home/<int:developer_id>/allowNotification', allow_notification),

]

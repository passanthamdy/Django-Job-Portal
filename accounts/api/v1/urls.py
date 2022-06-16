from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import company_signup,developer_signup, user_logout
app_name='accounts'
urlpatterns = [
    path('login', obtain_auth_token),
    path('user_logout', user_logout, obtain_auth_token),
    path('developer_signup', developer_signup, name='developer_signup'),
    path('company_signup', company_signup, name='company_signup'),
]

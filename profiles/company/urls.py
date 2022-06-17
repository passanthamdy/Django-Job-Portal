from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('home/<int:company_id>/details', views.get_company),
    path('home/<int:pk>/update', views.UpdataProfile.as_view()),
    path('home/<int:company_id>/allowNotification', views.allow_notification),
    path('home/<int:id>/history', views.get_history),

]

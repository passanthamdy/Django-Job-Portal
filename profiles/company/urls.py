from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('<int:company_id>/details/', views.get_company),
    path('<int:pk>/update/', views.UpdataProfile.as_view()),
    path('<int:company_id>/allow_notification/', views.allow_notification),
    path('<int:id>/history/', views.get_history),

]

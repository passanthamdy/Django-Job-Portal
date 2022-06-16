from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('home/create', views.create_company),
    path('home/<int:company_id>/details', views.get_company),
    path('home/<int:company_id>/update', views.update_company),

]

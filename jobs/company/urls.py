from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    #Company urls >> jobs/company/co...
    path('company-jobs/', views.ListCompanyJobs.as_view()),
    path('company-jobs/<int:pk>/', views.RetrieveUpdateDeleteCompanyJob.as_view()),
    path('company-jobs/<int:pk>/accept/',views.AcceptDeveloper)




]
from django.urls import path, include
from .developer.views import jobs_list_for_developer, job_details

app_name = 'jobs'

urlpatterns = [
    path('company/',include('jobs.company.urls')),
    path("developer/", include("jobs.developer.urls"))
]
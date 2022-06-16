from django.urls import path, include
from .developer.views import jobs_list_for_developer, job_details

app_name = 'jobs'

urlpatterns = [
    # Company urls

    # Developer urls
    path("developer/", include("jobs.developer.urls"))
]
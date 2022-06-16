from django.urls import path
from .views import jobs_list_for_developer, job_details,apply_for_job
app_name = 'jobs'

urlpatterns = [
    path("", jobs_list_for_developer, name="home"),
    path('<int:job_id>', job_details, name="details"),
    path('<int:job_id>/apply', apply_for_job, name="apply")
]
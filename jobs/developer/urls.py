from django.urls import path
from .views import jobs_list_for_developer, job_details,apply_for_job, mark_finish, current_job

app_name = 'jobs'

urlpatterns = [
    path("dev-jobs/", jobs_list_for_developer, name="home"),
    path("dev-jobs/current-job/",current_job , name="home"),
    path('dev-jobs/<int:job_id>/', job_details, name="details"),
    path('dev-jobs/<int:job_id>/apply/', apply_for_job, name="apply"),
    path('dev-jobs/<int:job_id>/finish/', mark_finish , name="finish-job")
]
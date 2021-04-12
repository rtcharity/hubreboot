from django.urls import path

from eahub.jobs.views import JobCreateView, jobs_list_view

app_name = "jobs"

urlpatterns = [
    path("", jobs_list_view, name="list"),
    path("create/", JobCreateView.as_view(), name="create"),
]

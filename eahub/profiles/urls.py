from django.urls import include, path

from . import views

app_name = "profiles_app"

urlpatterns = [
    path("", views.my_profile, name="my_profile"),
    path("edit/", views.edit_profile, name="edit_profile"),
    path(
        "edit/cause_areas/",
        views.edit_profile_cause_areas,
        name="edit_profile_cause_areas",
    ),
    path("edit/career/", views.edit_profile_career, name="edit_profile_career"),
    path(
        "edit/community/", views.edit_profile_community, name="edit_profile_community"
    ),
    path("delete/", views.delete_profile, name="delete_profile"),
    path(
        "<int:legacy_record>/",
        views.profile_redirect_from_legacy_record,
        name="profile_legacy",
    ),
    path("<slug:slug>/", views.profile_detail_or_redirect, name="profile"),
    path(
        "<slug:slug>/report-abuse/",
        views.ReportProfileAbuseView.as_view(),
        name="report_abuse_profile",
    ),
    path(
        "<slug:slug>/message/",
        views.SendProfileMessageView.as_view(),
        name="message_profile",
    ),
    path("api/", include("eahub.profiles.api.urls", namespace="api")),
]

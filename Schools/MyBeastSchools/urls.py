from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_subjects/", views.add_subject, name="add_subjects"),
    path("subjects/", views.get_subjects, name="get_subjects"),
    path("subjects/", views.get_subjects, name="get_students"),
    path("add_student/", views.add_student, name="add_student"),
]
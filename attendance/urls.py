from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("api/new-user", views.new_user, name="new-user"),
]
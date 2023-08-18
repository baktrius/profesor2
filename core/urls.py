from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /core/5/
    path("<int:temp_id>/", views.lesson, name="detail"),
]
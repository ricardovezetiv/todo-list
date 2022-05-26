from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("complete/<int:todo_id>", views.task_complete, name="complete"),
    path("incomplete/<int:todo_id>", views.task_incomplete, name="incomplete"),
    path("edit/<int:todo_id>", views.edit, name="edit"),
]

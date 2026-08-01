from django.urls import path

from . import views
from .views import submit_feedback

from .knowledge_views import (
    admin_panel,
    knowledge_base,
    add_knowledge,
    edit_knowledge,
    delete_knowledge,
)

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "feedback/",
        submit_feedback,
        name="feedback"
    ),

    path(
        "panel/",
        admin_panel,
        name="admin_panel"
    ),

    path(
        "knowledge/",
        knowledge_base,
        name="knowledge_base"
    ),

    path(
        "knowledge/add/",
        add_knowledge,
        name="add_knowledge"
    ),

    path(
        "knowledge/edit/<int:pk>/",
        edit_knowledge,
        name="edit_knowledge"
    ),

    path(
        "knowledge/delete/<int:pk>/",
        delete_knowledge,
        name="delete_knowledge"
    ),

]
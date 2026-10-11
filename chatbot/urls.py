from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import submit_feedback, clear_chat
from .knowledge_views import (
    knowledge_base,
    add_knowledge,
    edit_knowledge,
    delete_knowledge,
)

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        views.PreserveChatLogoutView.as_view(
            next_page="login"
        ),
        name="logout"
    ),

    path(
        "feedback/",
        submit_feedback,
        name="feedback"
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
    path(
    "clear-chat/",
    clear_chat,
    name="clear_chat"
    ),
    path(
    "chat-history/",
    views.chat_history,
    name="chat_history"
    ),
    path(

    "feedback-list/",

    views.feedback_list,

    name="feedback_list"

    ),
    path(

    "unanswered/",

    views.unanswered_questions,

    name="unanswered_questions"

    ),
    path(
    "admin-panel/",
    views.admin_panel,
    name="admin_panel"
    ),
]
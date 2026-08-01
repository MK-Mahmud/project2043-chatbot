from django.contrib import admin
from .models import (
    Intent,
    KnowledgeBase,
    ChatHistory,
    Feedback,
    UnansweredQuery
)


@admin.register(Intent)
class IntentAdmin(admin.ModelAdmin):
    list_display = ("intent_name", "description")
    search_fields = ("intent_name",)


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ("question_en", "intent")
    search_fields = ("question_en", "question_ha")
    list_filter = ("intent",)


@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "message",
        "intent",
        "language",
        "sentiment",
        "timestamp",
    )

    search_fields = (
        "message",
        "response",
        "intent",
    )

    list_filter = (
        "intent",
        "language",
        "sentiment",
    )

    ordering = ("-timestamp",)
    readonly_fields = ("timestamp",)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "chat",
        "rating",
        "comment",
    )

    search_fields = (
        "comment",
    )

    list_filter = (
        "rating",
    )


@admin.register(UnansweredQuery)
class UnansweredQueryAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "language",
        "status",
        "date_submitted",
    )

    search_fields = ("question",)

    list_filter = (
        "language",
        "status",
    )

    ordering = ("-date_submitted",)

    readonly_fields = ("date_submitted",)
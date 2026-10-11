from django.contrib import admin
from .models import (
    Intent,
    KnowledgeBase,
    ChatHistory,
    Feedback,
    UnansweredQuery
)

admin.site.register(Intent)
admin.site.register(KnowledgeBase)
admin.site.register(ChatHistory)
admin.site.register(Feedback)
admin.site.register(UnansweredQuery)
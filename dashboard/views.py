from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone

from chatbot.models import (
    ChatHistory,
    Feedback,
    KnowledgeBase,
    UnansweredQuery,
)


@login_required
def dashboard_home(request):
    """
    Administrator Dashboard
    """

    today = timezone.now().date()

    # ==========================
    # SUMMARY STATISTICS
    # ==========================

    total_chats = ChatHistory.objects.count()

    todays_chats = ChatHistory.objects.filter(
        timestamp__date=today
    ).count()

    positive = ChatHistory.objects.filter(
        sentiment="Positive"
    ).count()

    neutral = ChatHistory.objects.filter(
        sentiment="Neutral"
    ).count()

    negative = ChatHistory.objects.filter(
        sentiment="Negative"
    ).count()

    english = ChatHistory.objects.filter(
        language="ENGLISH"
    ).count()

    hausa = ChatHistory.objects.filter(
        language="HAUSA"
    ).count()

    unanswered = UnansweredQuery.objects.count()

    knowledge_count = KnowledgeBase.objects.count()

    feedback_count = Feedback.objects.count()

    # ==========================
    # RECENT TABLES
    # ==========================

    recent_chats = (
        ChatHistory.objects
        .order_by("-timestamp")[:10]
    )

    recent_feedback = (
        Feedback.objects
        .select_related("chat")
        .order_by("-id")[:5]
    )

    recent_unanswered = (
        UnansweredQuery.objects
        .order_by("-date_submitted")[:5]
    )

    # ==========================
    # INTENT STATISTICS
    # ==========================

    intent_stats = (
        ChatHistory.objects
        .values("intent")
        .annotate(total=Count("intent"))
        .order_by("-total")
    )

    top_intent = intent_stats.first()

    # ==========================
    # CONTEXT
    # ==========================

    context = {

        "total_chats": total_chats,
        "todays_chats": todays_chats,

        "positive": positive,
        "neutral": neutral,
        "negative": negative,

        "english": english,
        "hausa": hausa,

        "unanswered": unanswered,

        "knowledge_count": knowledge_count,
        "feedback_count": feedback_count,

        "recent_chats": recent_chats,
        "recent_feedback": recent_feedback,
        "recent_unanswered": recent_unanswered,

        "intent_stats": intent_stats,
        "top_intent": top_intent,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )
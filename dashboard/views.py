from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from django.utils import timezone

from chatbot.models import ChatHistory, UnansweredQuery


@login_required
def dashboard_home(request):

    total_chats = ChatHistory.objects.count()

    today = timezone.now().date()

    todays_chats = ChatHistory.objects.filter(
        timestamp__date=today
    ).count()

    positive = ChatHistory.objects.filter(
        sentiment="Positive"
    ).count()

    negative = ChatHistory.objects.filter(
        sentiment="Negative"
    ).count()

    neutral = ChatHistory.objects.filter(
        sentiment="Neutral"
    ).count()

    english = ChatHistory.objects.filter(
        language="ENGLISH"
    ).count()

    hausa = ChatHistory.objects.filter(
        language="HAUSA"
    ).count()

    unanswered = UnansweredQuery.objects.count()

    recent_chats = ChatHistory.objects.order_by(
        "-timestamp"
    )[:15]

    # Most requested intent
    top_intent = (
        ChatHistory.objects
        .values("intent")
        .annotate(total=Count("intent"))
        .order_by("-total")
        .first()
    )

    # Intent statistics
    intent_stats = (
        ChatHistory.objects
        .values("intent")
        .annotate(total=Count("intent"))
        .order_by("-total")
    )

    context = {
        "total_chats": total_chats,
        "todays_chats": todays_chats,

        "positive": positive,
        "negative": negative,
        "neutral": neutral,

        "english": english,
        "hausa": hausa,

        "unanswered": unanswered,

        "recent_chats": recent_chats,

        "top_intent": top_intent,
        "intent_stats": intent_stats,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )
import random
from datetime import datetime
from .services.response_formatter import format_response
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .models import (
    Intent,
    KnowledgeBase,
    ChatHistory,
    Feedback,
    UnansweredQuery
)

from .services.intent_classifier import classify_intent
from .services.language_detector import detect_language
from .services.sentiment import analyze_sentiment


def home(request):

    response = ""

    conversation = request.session.get("conversation", [])

    if request.method == "POST":

        message = request.POST.get("message")

        language = detect_language(message)

        sentiment = analyze_sentiment(message)

        detected_intent = classify_intent(message)

        print("USER MESSAGE:", message)
        print("PREDICTED INTENT:", detected_intent)

        # ==========================
        # UNKNOWN REQUEST
        # ==========================

        if detected_intent == "UNKNOWN":

            UnansweredQuery.objects.create(
                question=message,
                language=language
            )

            if language == "HAUSA":

                response = """
Ban fahimci tambayarka ba.

Kana iya tambayata game da:

• Bude Asusu

• Lamuni

• Canja Kudi

• ATM Card

• Mobile Banking

• Reshen Banki
"""

            else:

                response = """
I'm sorry, I couldn't understand your request.

You can ask me about:

• Opening a Bank Account

• Loan Services

• Money Transfer

• ATM & Debit Cards

• Mobile Banking

• Branch Locations
"""

        # ==========================
        # NORMAL REQUEST
        # ==========================

        else:

            try:

                intent = Intent.objects.get(
                    intent_name=detected_intent
                )

                responses = KnowledgeBase.objects.filter(
                    intent=intent
                )

                if responses.exists():

                    kb = random.choice(list(responses))

                    if language == "HAUSA":
                        response = format_response(

    detected_intent,

    kb.answer_ha

)
                    else:
                        response = format_response(

     detected_intent,

    kb.answer_en

)

                else:

                    raise Intent.DoesNotExist

            except Intent.DoesNotExist:

                UnansweredQuery.objects.create(
                    question=message,
                    language=language
                )

                if language == "HAUSA":

                    response = """
Ban fahimci tambayarka ba.

Kana iya tambayata game da:

• Bude Asusu

• Lamuni

• Canja Kudi

• ATM Card

• Mobile Banking

• Reshen Banki
"""

                else:

                    response = """
I'm sorry, I couldn't understand your request.

You can ask me about:

• Opening a Bank Account

• Loan Services

• Money Transfer

• ATM & Debit Cards

• Mobile Banking

• Branch Locations
"""

        # ==========================
        # SAVE CHAT
        # ==========================

        chat = ChatHistory.objects.create(

            message=message,

            response=response,

            intent=detected_intent,

            language=language,

            sentiment=sentiment

        )

        conversation.append({

            "user": message,

            "bot": response,

            "time": datetime.now().strftime("%I:%M %p")

        })

        request.session["conversation"] = conversation

        request.session["last_chat_id"] = chat.id

    return render(

        request,

        "chatbot/home.html",

        {

            "conversation": conversation,

            "response": response,

            "chat_id": request.session.get("last_chat_id")

        }

    )


# ============================================
# FEEDBACK
# ============================================
@login_required
def submit_feedback(request):

    if request.method == "POST":

        chat_id = request.POST.get("chat_id")

        rating = request.POST.get("rating")

        comment = request.POST.get("comment", "")

        try:

            chat = ChatHistory.objects.get(id=chat_id)

            Feedback.objects.create(

                chat=chat,

                rating=int(rating),

                comment=comment

            )

            return JsonResponse({

                "success": True

            })

        except Exception:

            return JsonResponse({

                "success": False

            })

    return JsonResponse({

        "success": False

    })
def clear_chat(request):

    request.session["conversation"] = []

    if "last_chat_id" in request.session:
        del request.session["last_chat_id"]

    return redirect("home")
# ==========================================================
# CHAT HISTORY
# ==========================================================
@login_required
def chat_history(request):

    chats = ChatHistory.objects.order_by("-timestamp")

    return render(

        request,

        "chatbot/chat_history.html",

        {

            "chats": chats

        }

    )
# ==========================================================
# CUSTOMER FEEDBACK
# ==========================================================
@login_required
def feedback_list(request):

    feedbacks = Feedback.objects.select_related(

        "chat"

    ).order_by(

        "-id"

    )

    return render(

        request,

        "chatbot/feedback.html",

        {

            "feedbacks": feedbacks

        }

    )
# ==========================================================
# UNANSWERED QUESTIONS
# ==========================================================
@login_required
def unanswered_questions(request):

    unanswered = UnansweredQuery.objects.order_by(

        "-date_submitted"

    )

    return render(

        request,

        "chatbot/unanswered_questions.html",

        {

            "unanswered": unanswered

        }

    )
@login_required
def admin_panel(request):

    context = {

        "total_chats": ChatHistory.objects.count(),

        "total_feedback": Feedback.objects.count(),

        "knowledge": KnowledgeBase.objects.count(),

        "unanswered": UnansweredQuery.objects.count(),

    }

    return render(
        request,
        "chatbot/admin_panel.html",
        context
    )


# ==========================================================
# LOGOUT (preserves the customer chat widget's conversation)
# ==========================================================
class PreserveChatLogoutView(LogoutView):
    """
    Django's default logout flushes the entire session, which would
    also wipe the customer chat conversation stored under the
    "conversation" session key. Since the admin dashboard and the
    customer chat widget share the same session in this project (both
    run in one browser during local testing/demo use), logging an
    administrator out would otherwise clear whatever conversation was
    on screen. This subclass carries the conversation across the
    logout so the chat widget isn't affected by an admin session
    ending.
    """

    def post(self, request, *args, **kwargs):
        conversation = request.session.get("conversation")
        last_chat_id = request.session.get("last_chat_id")

        response = super().post(request, *args, **kwargs)

        if conversation is not None:
            request.session["conversation"] = conversation
        if last_chat_id is not None:
            request.session["last_chat_id"] = last_chat_id

        return response
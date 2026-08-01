from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Intent,
    KnowledgeBase,
    ChatHistory,
    Feedback,
    UnansweredQuery
)


# ==========================================================
# ADMIN PANEL
# ==========================================================

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
# KNOWLEDGE BASE
# ==========================================================

def knowledge_base(request):

    knowledge = KnowledgeBase.objects.select_related(

        "intent"

    ).order_by(

        "intent__intent_name"

    )

    return render(

        request,

        "chatbot/knowledgebase.html",

        {

            "knowledge": knowledge

        }

    )


# ==========================================================
# ADD KNOWLEDGE
# ==========================================================

def add_knowledge(request):

    if request.method == "POST":

        intent = get_object_or_404(

            Intent,

            id=request.POST.get("intent")

        )

        KnowledgeBase.objects.create(

            intent=intent,

            question_en=request.POST.get("question_en"),

            question_ha=request.POST.get("question_ha"),

            answer_en=request.POST.get("answer_en"),

            answer_ha=request.POST.get("answer_ha")

        )

        return redirect("knowledge_base")

    intents = Intent.objects.all().order_by("intent_name")

    return render(

        request,

        "chatbot/add_knowledge.html",

        {

            "intents": intents

        }

    )


# ==========================================================
# EDIT KNOWLEDGE
# ==========================================================

def edit_knowledge(request, pk):

    knowledge = get_object_or_404(

        KnowledgeBase,

        pk=pk

    )

    if request.method == "POST":

        knowledge.intent = get_object_or_404(

            Intent,

            id=request.POST.get("intent")

        )

        knowledge.question_en = request.POST.get("question_en")

        knowledge.question_ha = request.POST.get("question_ha")

        knowledge.answer_en = request.POST.get("answer_en")

        knowledge.answer_ha = request.POST.get("answer_ha")

        knowledge.save()

        return redirect("knowledge_base")

    intents = Intent.objects.all().order_by("intent_name")

    return render(

        request,

        "chatbot/edit_knowledge.html",

        {

            "knowledge": knowledge,

            "intents": intents

        }

    )


# ==========================================================
# DELETE KNOWLEDGE
# ==========================================================

def delete_knowledge(request, pk):

    knowledge = get_object_or_404(

        KnowledgeBase,

        pk=pk

    )

    if request.method == "POST":

        knowledge.delete()

        return redirect("knowledge_base")

    return render(

        request,

        "chatbot/delete_knowledge.html",

        {

            "knowledge": knowledge

        }

    )
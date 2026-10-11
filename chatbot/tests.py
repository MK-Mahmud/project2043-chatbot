from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Intent, KnowledgeBase
from .services.intent_classifier import classify_intent
from .services.language_detector import detect_language
from .services.sentiment import analyze_sentiment


class IntentClassifierTests(TestCase):
    """Sanity checks for the trained intent classification model."""

    def test_greeting_is_recognized(self):
        self.assertEqual(classify_intent("Hello"), "GREETING")

    def test_loan_inquiry_is_recognized(self):
        self.assertEqual(classify_intent("I need a loan"), "LOAN_INQUIRY")

    def test_very_short_input_is_unknown(self):
        self.assertEqual(classify_intent("hi"), "UNKNOWN")

    def test_symbols_only_input_is_unknown(self):
        self.assertEqual(classify_intent("!!!123"), "UNKNOWN")


class LanguageDetectorTests(TestCase):
    """Sanity checks for the trained language detection model."""

    def test_english_message_detected(self):
        self.assertEqual(
            detect_language("What is my account balance?"), "ENGLISH"
        )

    def test_hausa_message_detected(self):
        self.assertEqual(
            detect_language("Ina son bude asusu"), "HAUSA"
        )


class SentimentAnalysisTests(TestCase):
    """Sanity checks for the rule-based sentiment classifier."""

    def test_positive_message(self):
        self.assertEqual(analyze_sentiment("Thank you, excellent service"), "Positive")

    def test_negative_message(self):
        self.assertEqual(analyze_sentiment("This is terrible, my card is blocked"), "Negative")

    def test_neutral_message(self):
        self.assertEqual(analyze_sentiment("I want to open an account"), "Neutral")


class ChatViewTests(TestCase):
    """Smoke tests for the customer-facing chat interface."""

    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_chatbot_responds_to_known_intent(self):
        intent = Intent.objects.create(intent_name="GREETING")
        KnowledgeBase.objects.create(
            intent=intent,
            question_en="Hello",
            question_ha="Sannu",
            answer_en="Hello! Welcome to ABC Bank.",
            answer_ha="Sannu! Barka da zuwa ABC Bank.",
        )
        response = self.client.post(reverse("home"), {"message": "Hello"})
        self.assertEqual(response.status_code, 200)


class AdminAccessTests(TestCase):
    """Confirm administrative pages are protected behind login."""

    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_user(
            username="testadmin", password="test-pass-123"
        )

    def test_admin_panel_requires_login(self):
        response = self.client.get(reverse("admin_panel"))
        self.assertNotEqual(response.status_code, 200)

    def test_knowledge_base_requires_login(self):
        response = self.client.get(reverse("knowledge_base"))
        self.assertNotEqual(response.status_code, 200)

    def test_admin_panel_accessible_when_logged_in(self):
        self.client.login(username="testadmin", password="test-pass-123")
        response = self.client.get(reverse("admin_panel"))
        self.assertEqual(response.status_code, 200)

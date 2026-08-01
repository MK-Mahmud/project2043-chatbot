from django.core.management.base import BaseCommand
from chatbot.models import Intent, KnowledgeBase


class Command(BaseCommand):
    help = "Populate the Knowledge Base with sample banking data"

    def handle(self, *args, **kwargs):

        data = [

            {
                "intent": "GREETING",
                "question_en": "Hello",
                "question_ha": "Sannu",
                "answer_en": "Hello! Welcome to ABC Bank. How may I assist you today?",
                "answer_ha": "Sannu! Barka da zuwa ABC Bank. Ta yaya zan taimake ka?"
            },

            {
                "intent": "GREETING",
                "question_en": "Good morning",
                "question_ha": "Ina kwana",
                "answer_en": "Good morning! Welcome to ABC Bank.",
                "answer_ha": "Ina kwana! Barka da zuwa ABC Bank."
            },

            {
                "intent": "ACCOUNT_OPENING",
                "question_en": "How do I open an account?",
                "question_ha": "Yaya zan bude asusu?",
                "answer_en": "Visit any ABC Bank branch with a valid ID, proof of address and passport photographs.",
                "answer_ha": "Je zuwa reshen ABC Bank tare da katin shaida, hujjar adireshi da hoton fasfo."
            },

            {
                "intent": "ACCOUNT_OPENING",
                "question_en": "What documents do I need to open an account?",
                "question_ha": "Wadanne takardu ake bukata domin bude asusu?",
                "answer_en": "You need a valid means of identification, proof of address and passport photographs.",
                "answer_ha": "Ana bukatar katin shaida, hujjar adireshi da hoton fasfo."
            },

            {
                "intent": "LOAN_INQUIRY",
                "question_en": "How do I apply for a loan?",
                "question_ha": "Yaya zan nemi rance?",
                "answer_en": "Visit the nearest ABC Bank branch or apply through our digital banking platform.",
                "answer_ha": "Je zuwa reshen ABC Bank mafi kusa ko amfani da dandalin bankinmu na yanar gizo."
            },

            {
                "intent": "ACCOUNT_BALANCE",
                "question_en": "How can I check my account balance?",
                "question_ha": "Yaya zan duba ma'aunin asusuna?",
                "answer_en": "You can check your balance using mobile banking, internet banking or an ATM.",
                "answer_ha": "Za ka iya duba ma'aunin asusunka ta Mobile Banking, Internet Banking ko ATM."
            },

            {
                "intent": "MONEY_TRANSFER",
                "question_en": "How do I transfer money?",
                "question_ha": "Yaya zan tura kudi?",
                "answer_en": "Transfers can be made using our mobile app, internet banking or at any branch.",
                "answer_ha": "Za ka iya tura kudi ta Mobile App, Internet Banking ko reshen banki."
            },

            {
                "intent": "CARD_SERVICE",
                "question_en": "I lost my ATM card.",
                "question_ha": "Na rasa katin ATM dina.",
                "answer_en": "Immediately block your card using the mobile app or contact customer support.",
                "answer_ha": "Gaggauta rufe katin ta Mobile App ko tuntubi sashen kula da kwastomomi."
            },

            {
                "intent": "BANK_HOURS",
                "question_en": "What are your working hours?",
                "question_ha": "Menene lokutan aiki?",
                "answer_en": "ABC Bank operates Monday to Friday from 8:00 AM to 4:00 PM.",
                "answer_ha": "ABC Bank yana aiki daga Litinin zuwa Juma'a daga karfe 8:00 na safe zuwa 4:00 na yamma."
            },

            {
                "intent": "FAREWELL",
                "question_en": "Thank you",
                "question_ha": "Na gode",
                "answer_en": "You're welcome! Thank you for choosing ABC Bank.",
                "answer_ha": "Babu komai! Mun gode da zabar ABC Bank."
            }

        ]

        for item in data:

            intent, _ = Intent.objects.get_or_create(
                intent_name=item["intent"]
            )

            KnowledgeBase.objects.get_or_create(
                intent=intent,
                question_en=item["question_en"],
                question_ha=item["question_ha"],
                defaults={
                    "answer_en": item["answer_en"],
                    "answer_ha": item["answer_ha"],
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Knowledge Base populated successfully."
            )
        )
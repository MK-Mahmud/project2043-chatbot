from django.db import models


class Intent(models.Model):
    intent_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.intent_name


class KnowledgeBase(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    question_en = models.TextField()
    question_ha = models.TextField()
    answer_en = models.TextField()
    answer_ha = models.TextField()

    def __str__(self):
        return self.question_en


class ChatHistory(models.Model):
    message = models.TextField()
    response = models.TextField()
    language = models.CharField(max_length=20)
    sentiment = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Feedback(models.Model):
    chat = models.ForeignKey(ChatHistory, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return str(self.rating)


class UnansweredQuery(models.Model):
    question = models.TextField()
    language = models.CharField(max_length=20)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.question

# Create your models here.

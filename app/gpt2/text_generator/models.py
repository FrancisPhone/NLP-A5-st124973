from django.db import models


class ChatMessage(models.Model):
    SENDER_CHOICES = [
        ("user", "User"),
        ("model", "Model"),
    ]

    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.capitalize()}: {self.text[:50]}"


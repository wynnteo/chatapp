from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chat_message"
        ordering = ('timestamp',)

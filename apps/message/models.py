from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class TelegramMessage(models.Model):
    message = models.TextField(blank=True, null=True)
    user = models.ForeignKey(to=User,
                                on_delete=models.CASCADE,
                                related_name='messages')
    created_date = models.DateTimeField(auto_now=True)
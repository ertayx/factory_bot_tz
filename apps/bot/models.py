from django.db import models


class CLient(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    chat_id = models.CharField(max_length=100)
    token_api = models.CharField(max_length=255, unique=True, null=True)
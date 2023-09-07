from django.core.management.base import BaseCommand

from apps.bot.main import start_bot


class Command(BaseCommand):
    help = "runner telegram bot"

    def handle(self, *args, **options):
        start_bot()
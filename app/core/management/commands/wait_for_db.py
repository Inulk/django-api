"""
Django command to wait for the DB to available
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    # Django command to waid for DB
    def handle(self, *args, **options):
        pass
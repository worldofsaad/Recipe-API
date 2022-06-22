"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Pscopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pscopg2OpError, OperationalError):
                self.stdout.write('Database unavailable. Waiting 1 sec..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Successfully connected'))

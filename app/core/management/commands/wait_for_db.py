"""
Django command to pause execution until database is available
"""
from django.core.management.base import BaseCommand
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand # noqa


class Command(BaseCommand):
    """Django command to wait for database"""

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for database...')
        db_conn = False
        while db_conn is False:
            try:
                self.check(databases=["default"])
                db_conn = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR('Database unavailable,'
                                                   ' reconnecting...'))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))

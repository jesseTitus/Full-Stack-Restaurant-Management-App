import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                db_conn.cursor().execute('SELECT 1')
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 1 second...')
                db_conn = None
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))

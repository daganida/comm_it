"""
This module represents sub command load_workers for inserting records from csv to database
"""
import csv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import logging

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Imports workers records from csv file and insert them to database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        """
        Should parse the csv file into user records and insert them to database
        """
        file_path = options['file_path']
        try:
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                user_records = [record for record in reader]
                for user_record in user_records:
                    try:
                        User.objects.create(
                            first_name=user_record['FirstName'],
                            last_name=user_record['LastName'],
                            username=user_record['Username'],
                            password=user_record['Password']
                        )
                    except Exception:
                        logger.exception('Could not create  %s' % user_record['Username'])
        except Exception:
            raise CommandError('Could not import worker records from file %s' % file_path)

        self.stdout.write(self.style.SUCCESS('Successfully imported tasks and workers from file %s ' % file_path))
import csv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Imports workers records from csv file and insert them to database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        """
        Should parse the csv file into user records and insert them to database
        """
        file_path = options['file_path']
        try:
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                user_records = [record for record in reader]
                # The first three rows contain irrelevant data
                for user_record in user_records:
                    if user_record['Username']:
                        try:
                            User.objects.create(first_name=user_record['FirstName'], last_name=user_record['LastName'],
                                                username=user_record['Username'], password=user_record['Password'])
                        except Exception as e:
                            print 'Could not create  %s' % user_record['Username']
        except Exception as e:
            raise CommandError('Could not import from file %s' % file_path)
        self.stdout.write(self.style.SUCCESS('Successfully imported tasks and workers from file %s ' % file_path))
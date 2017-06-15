import csv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Imports workers and tasks from csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        try:
            with open(file_path) as csvfile:
                reader = csv.DictReader(csvfile)
                data_rows = [row for row in reader]
                # The first three rows contain irrelevant data
                for data_row in data_rows:
                    if data_row['Username']:
                        try:
                            User.objects.create(first_name=data_row['FirstName'],last_name=data_row['LastName'],
                                                username=data_row['Username'],password=data_row['Password'])
                        except Exception as e:
                            print 'Could not create %s %s' %(data_row['Username'])
        except Exception as e:
            raise CommandError('Could not import from file %s' % file_path)
        self.stdout.write(self.style.SUCCESS('Successfully imported tasks and workers from file %s ' % file_path))
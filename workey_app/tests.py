import argparse

from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO

from workey_app.models import Worker


class CommandsTestCase(TestCase):

    def test_load_workers_command(self):
        "Should test load_workers command perform insertion of all records into the database."
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument('-file_path','--/Users/idandagan/Desktop/data_csv.csv' )
        parser = argparse.ArgumentParser(add_help=False)
        opts = parser.parse_args()
        workers_count = Worker.objects.all().count()
        self.assertEqual(workers_count, 0)
        out = StringIO()
        call_command('load_workers', stdout=out, **opts)
        self.assertIn('Expected output', out.getvalue())
        import csv
        with open(opts['file_path']) as csvfile:
            reader = csv.DictReader(csvfile)
            user_records = [record for record in reader]
            records_number = len(user_records)
            self.assertEqual(records_number, Worker.objects.all().count())


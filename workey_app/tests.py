from django.test import TestCase
from django.core.management import call_command
from django.utils.six import StringIO
from workey_app.models import Worker


class CommandsTestCase(TestCase):

    def test_load_workers_command(self):
        "Should test load_workers command perform insertion of all records into the database."
        workers_count = Worker.objects.all().count()
        self.assertEqual(workers_count, 0)
        file_path = 'test_data.csv'
        args = [file_path]
        out = StringIO()
        opts = {}
        call_command('load_workers', stdout=out, *args, **opts)
        self.assertIn('Successfully', out.getvalue())
        import csv
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            user_records = [record for record in reader]
            records_number = len(user_records)
            self.assertEqual(records_number, Worker.objects.all().count())

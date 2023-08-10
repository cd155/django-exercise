from django.test import TestCase
from .models import Logger
from datetime import datetime
from django.utils import timezone

# Create your tests here.


class LoggerTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Logger.objects.create(
            first_name="Ted",
            last_name="Li",
            time_log=timezone.now(),
            date_log=timezone.now()
        )

    def test_logger_types(self):
        tedli = Logger.objects.get(
            first_name="Ted",
            last_name="Li",
        )
        self.assertIsInstance(tedli.date_log, datetime)

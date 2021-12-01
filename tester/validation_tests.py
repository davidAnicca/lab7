import datetime
from unittest import TestCase

from validation.event_validator import EventValidator
from validation.validation_error import ValidationError


class ValidationTests(TestCase):

    def test_validate_event(self):

        event_validator = EventValidator()
        event_validator.validate_date(datetime.date.today() + datetime.timedelta(days=3))
        self.assertRaises(ValidationError,
                          event_validator.validate_date,
                          datetime.date.today() - datetime.timedelta(days=2))

import datetime
from unittest import TestCase

from validation.event_validator import EventValidator
from validation.validation_error import ValidationError


class ValidationTests(TestCase):
    def __init__(self):
        pass

    def test_validate_event(self):
        event_validator = EventValidator()
        try:
            event_validator.validate_date(datetime.date.today() + datetime.timedelta(days=3))
        except Exception:
            self.fail()
        try:
            event_validator.validate_date(datetime.date.today() - datetime.timedelta(days=2))
            self.fail()
        except ValidationError as e:
            if str(e) != "nu se poate crea un eveniment în trecut":
                self.fail()
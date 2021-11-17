import datetime

from domain.event import Event
from validation.validation_error import ValidationError


class EventValidator(object):

    def validate_date(self, date):
        """
        tests if a date is logically valid for an event
        :param date: given date
        :return:
        :raises: ValidateError with message "nu se poate crea un eveniment în trecut"
            if the given date is in the past
        """
        if date < datetime.date.today():
            raise ValidationError("nu se poate crea un eveniment în trecut")
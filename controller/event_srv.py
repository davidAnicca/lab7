import datetime

from domain.event import Event
from repo.event_repo import EventRepo
from repo.sale_repo import SaleRepo
from validation.event_validator import EventValidator


class EventService(object):
    def __init__(self, event_repo: EventRepo, sale_repo: SaleRepo):
        self.__event_repo = event_repo
        self.__sale_repo = sale_repo

    def create_event(self, e_id, e_date, e_duration, e_description):
        """
        creates an event based on information
        :param e_id: event id
        :param e_date: event date
        :param e_duration: event duration
        :param e_description: event description
        :raises: ValidationError if date is not valid
        """
        EventValidator().validate_date(e_date)
        return Event(e_id, e_date, e_duration, e_description)

    def add_event(self, e_id: int, e_date: datetime.date, e_duration: int, e_description):
        """
        asks repo to add an event in list
        :param e_id: event id
        :param e_date: event date
        :param e_duration: event duration
        :param e_description: event description
        :return:
        """
        event = self.create_event(e_id, e_date, e_duration, e_description)
        self.__event_repo.add(event)

    def delete_event(self, e_id: int):
        """
        deletes an event based on id
        :param e_id: event id
        :raises: RepoError if event cannot be found
        """
        event = self.__event_repo.find_by_id(e_id)
        self.__event_repo.delete(event, self.__sale_repo)

    def modify_date(self, e_id, e_date):
        """
        modifies the date for event with id
        :param e_id: id
        :param e_date: new date
        :raises: RepoError if event cannot be found or ValidateError if date is invalid
        """
        EventValidator.validate_date(e_date)
        event = self.__event_repo.find_by_id(e_id)
        self.__event_repo.modify_date(event, e_date)

    def modify_duration(self, e_id, e_duration):
        """
        modifies duration for event with id
        :param e_id: id
        :param e_duration: new duration
        :raises: RepoError if event cannot be found
        """
        event = self.__event_repo.find_by_id(e_id)
        self.__event_repo.modify_duration(event, e_duration)

    def modify_description(self, e_id, e_description):
        """
        modifies description for event with id
        :param e_id: id
        :param e_description: new description
        :return: RepoError if event cannot be found
        """
        event = self.__event_repo.find_by_id(e_id)
        self.__event_repo.modify_description(event, e_description)

    def get_all(self):
        return self.__event_repo.get_all()
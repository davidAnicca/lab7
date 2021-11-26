import datetime

from domain.event import Event
from logic.event_logic import EventLogic
from repo.event_repo import EventRepo
from repo.sale_repo import SaleRepo
from validation.event_validator import EventValidator


class EventService(object):
    def __init__(self, event_repo: EventRepo, sale_repo: SaleRepo):
        self.__event_repo = event_repo
        self.__sale_repo = sale_repo

    def find(self, e_id):
        return self.__event_repo.find(Event(e_id, datetime.datetime.today(), 2, "a"))

    def first_3_events(self):
        """
        shows the first 3 events with biggest num of participants
        :return: a list of events
        """
        events_w_participants = {}
        events = self.__event_repo.get_all()
        sales = self.__sale_repo.get_all()
        for event in events:
            for sale in sales:
                if sale.get_event() == event:
                    if event.get_id() not in events_w_participants.keys():
                        events_w_participants.update({event.get_id(): 0})
                    else:
                        events_w_participants[event.get_id()] += 1
        sort_events = sorted(events_w_participants.items(), key=lambda x: x[1], reverse=True)
        new_events = []
        for elem in sort_events:
            new_events.append(self.__event_repo.find(Event(elem[0], datetime.date.today(), 1, "a")))
        if len(new_events) < 3:
            return new_events
        return new_events[:3]

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
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        self.__event_repo.delete(event, self.__sale_repo)

    def modify_date(self, e_id, e_date):
        """
        modifies the date for event with id
        :param e_id: id
        :param e_date: new date
        :raises: RepoError if event cannot be found or ValidateError if date is invalid
        """
        EventValidator.validate_date(e_date)
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        self.__event_repo.modify(Event(e_id, e_date, event.get_duration(), event.get_description()))

    def modify_duration(self, e_id, e_duration):
        """
        modifies duration for event with id
        :param e_id: id
        :param e_duration: new duration
        :raises: RepoError if event cannot be found
        """
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        self.__event_repo.modify(Event(e_id, event.get_date(), e_duration, event.get_description()))

    def modify_description(self, e_id, e_description):
        """
        modifies description for event with id
        :param e_id: id
        :param e_description: new description
        :return: RepoError if event cannot be found
        """
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        self.__event_repo.modify(Event(e_id, event.get_date(), event.get_duration(), e_description))

    def soldouts(self):
        logic = EventLogic(self.__event_repo, self.__sale_repo)
        return logic.get_first_20_p_with_participants()

    def get_all(self):
        return self.__event_repo.get_all()

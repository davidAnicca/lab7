import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from logic.event_logic import EventLogic
from repo.event_repo import EventRepo
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


class LogicTests(TestCase):
    def __init__(self):
        self.__test_events_repo = EventRepo([Event(1, datetime.date.today(), 1, "description1"),
                                             Event(2, datetime.date.today(), 6, "lol"),
                                             Event(3, datetime.date.today(), 1, "macarena")])
        self.__test_person_repo = PersonRepo([Person(1, "marcel", "cluj"),
                                              Person(2, "cristian", "turda"),
                                              Person(3, "maria", "cluj"),
                                              Person(4, "ionel", "cluj")])
        self.__test_sale_repo = SaleRepo([Sale(self.__test_person_repo.get_all()[0],
                                               self.__test_events_repo.get_all()[1]),
                                          Sale(self.__test_person_repo.get_all()[1],
                                               self.__test_events_repo.get_all()[2]),
                                          Sale(self.__test_person_repo.get_all()[1],
                                               self.__test_events_repo.get_all()[0]),
                                          Sale(self.__test_person_repo.get_all()[1],
                                               self.__test_events_repo.get_all()[2]),
                                          Sale(self.__test_person_repo.get_all()[2],
                                               self.__test_events_repo.get_all()[2]),
                                          ])

    def test_get_event_w_max_duration(self):
        empty_repo = EventRepo([])
        event_logic = EventLogic(empty_repo)
        if event_logic.get_event_with_max_duration() is not None:
            self.fail()
        del event_logic
        event_logic = EventLogic(self.__test_events_repo)
        if event_logic.get_event_with_max_duration() != self.__test_events_repo.get_all()[1]:
            self.fail()

    def test_get_person_with_most_events(self):
        empty_repo = PersonRepo([])#todo
        self.fail()

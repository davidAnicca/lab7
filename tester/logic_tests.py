import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from logic.event_logic import EventLogic
from logic.person_logic import PersonLogic
from repo.event_repo import EventRepo
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


class LogicTests(TestCase):
    def __init__(self):
        self.__test_events_repo = EventRepo([Event(0, datetime.date.today(), 1, "a"),
                                             Event(1, datetime.date.today() + datetime.timedelta(days=20), 6, "c"),
                                             Event(2, datetime.date.today() + datetime.timedelta(days=10), 1, "b")])
        self.__test_person_repo = PersonRepo([Person(0, "marcel", "cluj"),
                                              Person(1, "cristian", "turda"),
                                              Person(2, "maria", "cluj"),
                                              Person(3, "ionel", "cluj")])
        self.__test_sale_repo = SaleRepo([Sale(self.__test_person_repo.get_all()[0],  # 0 2
                                               self.__test_events_repo.get_all()[2]),
                                          Sale(self.__test_person_repo.get_all()[1],  # 1 2
                                               self.__test_events_repo.get_all()[2]),
                                          Sale(self.__test_person_repo.get_all()[1],  # 1 0
                                               self.__test_events_repo.get_all()[0]),
                                          Sale(self.__test_person_repo.get_all()[1],  # 1 1
                                               self.__test_events_repo.get_all()[1]),
                                          Sale(self.__test_person_repo.get_all()[2],  # 2 2
                                               self.__test_events_repo.get_all()[2]),
                                          ])

    def test_get_20_p(self):
        event_logic = EventLogic(self.__test_events_repo, self.__test_sale_repo)
        events = event_logic.get_first_20_p_with_participants()
        if len(events) != 1:
            self.fail()
        if self.__test_events_repo.get_all()[2] != events[0]:
            self.fail()

    def test_get_event_w_max_duration(self):
        empty_repo = EventRepo([])
        event_logic = EventLogic(empty_repo, self.__test_sale_repo)
        if event_logic.get_event_with_max_duration() is not None:
            self.fail()
        del event_logic
        event_logic = EventLogic(self.__test_events_repo, self.__test_sale_repo)
        if event_logic.get_event_with_max_duration() != self.__test_events_repo.get_all()[1]:
            self.fail()

    def test_get_person_with_most_events(self):
        empty_repo = PersonRepo([])
        person_logic = PersonLogic(empty_repo, self.__test_sale_repo)
        if len(person_logic.get_person_with_most_events()) > 0:
            self.fail()
        person_logic = PersonLogic(self.__test_person_repo, self.__test_sale_repo)
        if self.__test_person_repo.get_all()[1] not in person_logic.get_person_with_most_events():
            self.fail()

    def test_give_all_events_ordered_by_date(self):
        person_logic = PersonLogic(self.__test_person_repo, self.__test_sale_repo)
        events = person_logic.get_all_my_events_ordered_by_date(self.__test_person_repo.get_all()[1])
        if self.__test_events_repo.get_all()[0] not in events \
                and self.__test_events_repo.get_all()[1] not in events and \
                self.__test_events_repo.get_all()[2] not in events:
            self.fail()
        if events[0] != self.__test_events_repo.get_all()[0] and events[1] != self.__test_events_repo.get_all()[2]:
            self.fail()
        if events[2] != self.__test_events_repo.get_all()[1]:
            self.fail()

    def test_give_all_events_ordered_by_description(self):
        person_logic = PersonLogic(self.__test_person_repo, self.__test_sale_repo)
        events = person_logic.get_all_my_events_ordered_by_duration(self.__test_person_repo.get_all()[1])
        if self.__test_events_repo.get_all()[0] not in events \
                and self.__test_events_repo.get_all()[1] not in events and \
                self.__test_events_repo.get_all()[2] not in events:
            self.fail()
        if events[0] != self.__test_events_repo.get_all()[0] and events[1] != self.__test_events_repo.get_all()[2]:
            self.fail()
        if events[2] != self.__test_events_repo.get_all()[1]:
            self.fail()

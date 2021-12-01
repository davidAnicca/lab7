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

    def setUp(self) -> None:
        self.test_events_repo = EventRepo([Event(0, datetime.date.today(), 1, "a"),
                                           Event(1, datetime.date.today() + datetime.timedelta(days=20), 6, "c"),
                                           Event(2, datetime.date.today() + datetime.timedelta(days=10), 1, "b")])
        self.test_person_repo = PersonRepo([Person(0, "marcel", "cluj"),
                                            Person(1, "cristian", "turda"),
                                            Person(2, "maria", "cluj"),
                                            Person(3, "ionel", "cluj")])
        self.test_sale_repo = SaleRepo([Sale(self.test_person_repo.get_all()[0],  # 0 2
                                             self.test_events_repo.get_all()[2]),
                                        Sale(self.test_person_repo.get_all()[1],  # 1 2
                                             self.test_events_repo.get_all()[2]),
                                        Sale(self.test_person_repo.get_all()[1],  # 1 0
                                             self.test_events_repo.get_all()[0]),
                                        Sale(self.test_person_repo.get_all()[1],  # 1 1
                                             self.test_events_repo.get_all()[1]),
                                        Sale(self.test_person_repo.get_all()[2],  # 2 2
                                             self.test_events_repo.get_all()[2]),
                                        ])

    def tearDown(self) -> None:
        del self.test_person_repo
        del self.test_events_repo
        del self.test_sale_repo

    def test_get_20_p(self):
        event_logic = EventLogic(self.test_events_repo, self.test_sale_repo)
        events = event_logic.get_first_20_p_with_participants()
        self.assertEqual(len(events), 1)
        self.assertEqual(self.test_events_repo.get_all()[2], events[0])

    def test_get_event_w_max_duration(self):
        empty_repo = EventRepo([])
        event_logic = EventLogic(empty_repo, self.test_sale_repo)
        self.assertIsNone(event_logic.get_event_with_max_duration())
        del event_logic
        event_logic = EventLogic(self.test_events_repo, self.test_sale_repo)
        self.assertEqual(event_logic.get_event_with_max_duration(), self.test_events_repo.get_all()[1])

    def test_get_person_with_most_events(self):
        empty_repo = PersonRepo([])
        person_logic = PersonLogic(empty_repo, self.test_sale_repo)
        self.assertEqual(len(person_logic.get_person_with_most_events()), 0)
        person_logic = PersonLogic(self.test_person_repo, self.test_sale_repo)
        self.assertGreater(len(person_logic.get_person_with_most_events()), 0)
        self.assertNotIn(self.test_person_repo.get_all()[0], person_logic.get_person_with_most_events())

    def test_give_all_events_ordered(self):
        person_logic = PersonLogic(self.test_person_repo, self.test_sale_repo)
        events_date = person_logic.get_all_my_events_ordered_by_date(self.test_person_repo.get_all()[1])
        events_duration = person_logic.get_all_my_events_ordered_by_date(self.test_person_repo.get_all()[1])
        lists = [events_date, events_duration]
        for col in lists:
            self.assertIn(self.test_events_repo.get_all()[0], col)
            self.assertIn(self.test_events_repo.get_all()[1], col)
            self.assertIn(self.test_events_repo.get_all()[2], col)
            self.assertEqual(col[0], self.test_events_repo.get_all()[0])
            self.assertEqual(col[1], self.test_events_repo.get_all()[2])
            self.assertEqual(col[2], self.test_events_repo.get_all()[1])

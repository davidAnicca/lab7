import datetime
import unittest
from unittest import TestCase

from controller.event_srv import EventService
from controller.person_srv import PersonService
from controller.sale_srv import SaleService
from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.event_repo import EventRepo
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo
from validation.event_validator import EventValidator
from validation.validation_error import ValidationError


class ControllerTest(TestCase):
    def setUp(self) -> None:
        self.events_repo = EventRepo([Event(0, datetime.date.today(), 1, "a"),
                                      Event(1, datetime.date.today() + datetime.timedelta(days=20), 6, "c"),
                                      # del
                                      Event(2, datetime.date.today() + datetime.timedelta(days=10), 1, "b"),
                                      Event(3, datetime.date.today() + datetime.timedelta(days=10), 1, "b")])
        self.person_repo = PersonRepo([Person(0, "marcel", "cluj"),
                                       Person(1, "cristian", "turda"),  # del
                                       Person(2, "maria", "cluj"),
                                       Person(3, "ionel", "cluj")])
        self.sale_repo = SaleRepo([Sale(self.person_repo.get_all()[0],  # 0 2        # 2 -3
                                        self.events_repo.get_all()[2]),  # 0 - 2
                                   Sale(self.person_repo.get_all()[1],  # 1 2        # 1 - 1
                                        self.events_repo.get_all()[2]),
                                   Sale(self.person_repo.get_all()[1],  # 1 0
                                        self.events_repo.get_all()[0]),
                                   Sale(self.person_repo.get_all()[1],  # 1 1
                                        self.events_repo.get_all()[1]),
                                   Sale(self.person_repo.get_all()[2],  # 2 2
                                        self.events_repo.get_all()[2]),
                                   Sale(self.person_repo.get_all()[2],  # 2 0
                                        self.events_repo.get_all()[0])
                                   ])
        self.person_srv = PersonService(self.person_repo, self.sale_repo)
        self.event_srv = EventService(self.events_repo, self.sale_repo)
        self.sale_srv = SaleService(self.person_repo, self.events_repo, self.sale_repo)

    def tearDown(self) -> None:
        del self.events_repo
        del self.person_repo
        del self.sale_repo
        del self.person_srv
        del self.event_srv
        del self.sale_srv

    def test_create_person(self):
        p_id = 4
        p_name = "nume"
        p_address = "adresaa"
        obj = self.person_srv.create_person(p_id, p_name, p_address)
        self.assertIsInstance(obj, Person)
        self.assertEqual(obj.get_id(), p_id)
        self.assertEqual(obj.get_name(), p_name)
        self.assertEqual(obj.get_address(), p_address)

    def test_add_person(self):
        p_id = 10
        p_name = "nume"
        p_address = "adresaa"
        self.assertRaises(RepoError, self.person_srv.add_person, 1, p_name, p_address)
        self.person_srv.add_person(p_id, p_name, p_address)
        person = self.person_repo.find(Person(p_id, p_name, p_address))
        self.assertEqual(person, Person(p_id, p_name, p_address))

    def test_delete(self):
        self.assertRaises(RepoError, self.person_srv.delete_person, 7)
        self.person_srv.delete_person(1)
        self.assertRaises(RepoError, self.person_repo.find, Person(1, "", ""))

    def test_modify(self):
        self.assertRaises(RepoError, self.person_srv.modify_name, 11, "name")
        self.assertRaises(RepoError, self.person_srv.modify_address, 11, "name")
        self.person_srv.modify_name(1, "name")
        self.person_srv.modify_address(1, "address")
        self.assertEqual(self.person_repo.find(Person(1, "", "")).get_name(), "name")
        self.assertEqual(self.person_repo.find(Person(1, "", "")).get_address(), "address")

    def test_create_event(self):
        e_id = 10
        e_date = datetime.date.today() - datetime.timedelta(days=10)
        e_duration = 3
        e_description = "descriere"
        self.assertRaises(ValidationError, self.event_srv.create_event, e_id, e_date, e_duration, e_description)
        e_date = e_date + datetime.timedelta(days=11)
        obj = self.event_srv.create_event(e_id, e_date, e_duration, e_description)
        self.assertIsInstance(obj, Event)
        self.assertEqual(obj.get_id(), e_id)
        self.assertEqual(obj.get_date(), e_date)
        self.assertEqual(obj.get_duration(), e_duration)
        self.assertEqual(obj.get_description(), e_description)

    def test_add_event(self):
        e_id = 10
        e_date = datetime.date.today()
        e_duration = 3
        e_description = "desc"
        self.assertRaises(RepoError,
                          self.event_srv.add_event,
                          1,
                          datetime.date.today() + datetime.timedelta(days=10),
                          e_duration,
                          e_description
                          )
        self.assertRaises(ValidationError,
                          self.event_srv.add_event,
                          1,
                          datetime.date.today() - datetime.timedelta(days=10),
                          e_duration,
                          e_description
                          )
        self.event_srv.add_event(e_id, e_date + datetime.timedelta(days=10), e_duration, e_description)
        event = self.events_repo.find(Event(e_id, e_date + datetime.timedelta(days=10), e_duration, e_description))
        events = self.events_repo.get_all()
        self.assertIn(event, events)

    def test_delete_event(self):
        self.assertRaises(RepoError, self.event_srv.delete_event, 9)
        self.event_srv.delete_event(1)
        event = Event(1, datetime.date.today() + datetime.timedelta(days=20), 6, "c")
        events = self.events_repo.get_all()
        self.assertNotIn(event, events)

    def test_modify_event(self):
        self.assertRaises(RepoError, self.event_srv.modify_date, 20,
                          datetime.date.today() + datetime.timedelta(days=10))
        self.assertRaises(RepoError, self.event_srv.modify_duration, 20,
                          2)
        self.assertRaises(RepoError, self.event_srv.modify_description, 20,
                          'a')
        self.assertRaises(ValidationError, self.event_srv.modify_date, 2,
                          datetime.date.today() - datetime.timedelta(days=10))
        self.event_srv.modify_date(2, datetime.date.today() + datetime.timedelta(days=10))
        self.event_srv.modify_duration(2, 3)
        self.event_srv.modify_description(2, "blabla")
        modified: Event = self.events_repo.find(Event(2, None, 0, ""))
        self.assertEqual(modified.get_date(), datetime.date.today() + datetime.timedelta(days=10))
        self.assertEqual(modified.get_duration(), 3)
        self.assertEqual(modified.get_description(), "blabla")

    def test_create_sale(self):
        self.assertRaises(RepoError, self.sale_srv.create_sale, 22, 1)
        self.assertRaises(RepoError, self.sale_srv.create_sale, 3, 22)
        sale: Sale = self.sale_srv.create_sale(2, 2)
        self.assertEqual(sale.get_person(), self.person_repo.find(Person(2, "a", "a")))
        self.assertEqual(sale.get_event(), self.events_repo.find(Event(2, None, 0, "")))

    def test_add_sale(self):
        self.assertRaises(RepoError, self.sale_srv.add_sale, 22, 1)
        self.assertRaises(RepoError, self.sale_srv.add_sale, 3, 22)
        self.assertRaises(RepoError, self.sale_srv.add_sale, 2, 2)
        self.sale_srv.add_sale(2, 1)
        sales = self.sale_repo.get_all()
        sale = self.sale_repo.find_by_pair(self.person_repo.find(Person(2, "a", "a")),
                                           self.events_repo.find(Event(1, None, 0, "")))
        self.assertIn(sale, sales)

    def test_delete_sale(self):
        self.assertRaises(RepoError, self.sale_srv.delete_sale, 22, 1)
        self.assertRaises(RepoError, self.sale_srv.delete_sale, 3, 22)
        self.assertRaises(RepoError, self.sale_srv.delete_sale, 2, 3)
        self.sale_srv.delete_sale(2, 0)
        self.assertRaises(RepoError, self.sale_srv.delete_sale, 2, 0)

    def test_top_3(self):
        top3 = self.event_srv.first_3_events()
        if len(top3) != 3:
            self.fail()
        self.assertEqual(top3[0], self.events_repo.find(Event(2, datetime.date.today(), 2, 'a')))
        self.assertEqual(top3[1], self.events_repo.find(Event(0, datetime.date.today(), 2, 'a')))
        self.assertEqual(top3[2], self.events_repo.find(Event(1, datetime.date.today(), 2, 'a')))

def run():
    unittest.main()

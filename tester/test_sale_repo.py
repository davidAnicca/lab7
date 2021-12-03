import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.dto.event_repo_dto import EventRepoDTO
from repo.dto.person_repo_dto import PersonRepoDTO
from repo.dto.sale_repo_dto import SaleRepoDTO
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class TestSaleRepo(TestCase):

    def setUp(self) -> None:
        file_path = 'tester/sales.txt'
        with open("tester/persons.csv", 'w') as f:
            f.write("")
            f.close()
        with open("tester/events.csv", 'w') as f:
            f.write("")
            f.close()
        with open("tester/sales.txt", 'w') as f:
            f.write("")
            f.close()
        self.person_repo = PersonRepoDTO([Person(1, "marcel", "address"), Person(2, "cristi", "address")],
                                         'tester/persons.csv')
        self.event_repo = EventRepoDTO([Event(1, datetime.date.today(), 2, "a"),
                                        Event(2, datetime.date.today(), 2, "2")],
                                       'tester/events.csv')

        self.test_repo = SaleRepoDTO([Sale(Person(1, "marcel", "address"), Event(1, datetime.date.today(), 2, "a")),
                                      Sale(Person(2, "cristi", "address"), Event(1, datetime.date.today(), 2, "a")),
                                      Sale(Person(2, "cristi", "address"), Event(2, datetime.date.today(), 2, "2"))],
                                     self.person_repo,
                                     self.event_repo,
                                     file_path)

    def tearDown(self) -> None:
        del self.person_repo
        del self.event_repo
        del self.test_repo

    def test_find(self):
        self.test_repo.assert_exist(self.test_repo.get_all()[0])
        self.assertRaises(RepoError, self.test_repo.assert_exist,
                          Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as")))

    def test_find_by_pair(self):
        sale: Sale = self.test_repo.get_all()[0]
        person: Person = sale.get_person()
        event: Event = sale.get_event()
        found_sale = self.test_repo.find_by_pair(person, event)
        self.assertIsNotNone(found_sale)
        sale = Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as"))
        person = sale.get_person()
        event = sale.get_event()
        found_sale = self.test_repo.find_by_pair(person, event)
        self.assertIsNone(found_sale)

    def test_add(self):
        self.person_repo.add(Person(7, "a", "a"))
        self.event_repo.add(Event(7, datetime.date.today(), 3, "as"))
        sale_to_add = Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as"))
        self.test_repo.add(sale_to_add)
        self.assertIn(sale_to_add, self.test_repo.get_all())
        sale_to_add = self.test_repo.get_all()[0]
        self.assertRaises(RepoError, self.test_repo.add, sale_to_add)

    def test_delete(self):
        sale_to_delete = Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as"))
        self.assertRaises(RepoError, self.test_repo.delete, sale_to_delete)
        sale_to_delete = self.test_repo.get_all()[0]
        self.test_repo.delete(sale_to_delete)
        self.assertNotIn(sale_to_delete, self.test_repo.get_all())

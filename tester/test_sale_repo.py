import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class TestSaleRepo(TestCase):

    def __init__(self):
        self.__test_repo = SaleRepo([Sale(Person(1, "marcel", "address"), Event(1, datetime.date.today(), 2, "a")),
                                     Sale(Person(2, "cristi", "address"), Event(1, datetime.date.today(), 2, "a")),
                                     Sale(Person(2, "cristi", "address"), Event(2, datetime.date.today(), 2, "2"))])

    def test_find(self):
        try:
            self.__test_repo.find(self.__test_repo.get_all()[0])
        except RepoError:
            self.fail()
        try:
            self.__test_repo.find(Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as")))
            self.fail()
        except RepoError as e:
            if str(e) != "participarea nu există":
                self.fail()

    def test_find_by_pair(self):
        sale: Sale = self.__test_repo.get_all()[0]
        person: Person = sale.get_person()
        event: Event = sale.get_event()
        found_sale = self.__test_repo.find_by_pair(person, event)
        if found_sale is None:
            self.fail()
        sale = Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as"))
        person = sale.get_person()
        event = sale.get_event()
        found_sale = self.__test_repo.find_by_pair(person, event)
        if found_sale is not None:
            self.fail()

    def test_add(self):
        sale_to_add = Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as"))
        self.__test_repo.add(sale_to_add)
        sale_to_add = self.__test_repo.get_all()[0]
        try:
            self.__test_repo.add(sale_to_add)
            self.fail()
        except RepoError as e:
            if str(e) != "participarea deja există":
                self.fail()

    def test_delete(self):
        sale_to_delete = Sale(Person(7, "a", "a"), Event(7, datetime.date.today(), 3, "as"))
        try:
            self.__test_repo.delete(sale_to_delete)
            self.fail()
        except RepoError as e:
            if str(e) != "participarea nu există":
                self.fail()

        sale_to_delete = self.__test_repo.get_all()[0]
        self.__test_repo.delete(sale_to_delete)
        if sale_to_delete in self.__test_repo.get_all()[0]:
            self.fail()





import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.event_repo import EventRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class TestEventRepo(TestCase):

    def __init__(self):
        self.__test_repo = EventRepo([Event(1, datetime.date.today(), 1, "description1"),
                                      Event(2, datetime.date.today(), 1, "lol"),
                                      Event(3, datetime.date.today(), 1, "macarena")])

    def test_find(self):
        event: Event = self.__test_repo.get_all()[0]
        try:
            self.__test_repo.find(event)
        except RepoError:
            self.fail()
        event = Event(0, datetime.datetime.today(), 1, "nu ex")
        try:
            self.__test_repo.find(event)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()



    def test_add(self):
        try:
            self.__test_repo.add(Event(5, datetime.datetime.today(), 1, "aaa"))
        except RepoError as e:
            self.fail()
        try:
            self.__test_repo.add(self.__test_repo.get_all()[0])
            self.fail()
        except RepoError as e:
            if str(e) != "id deja existent":
                self.fail()

    def test_modify(self):
        try:
            self.__test_repo.modify(Event(0, datetime.date.today(), 2, ""))
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()
        new_event = Event(5, datetime.date.today() + datetime.timedelta(days=2), 2, "new")
        self.__test_repo.modify(new_event)
        modified: Event = self.__test_repo.find(new_event)
        if modified.get_date() != datetime.date.today() + datetime.timedelta(days=2) or \
                modified.get_duration() != 2 or \
                modified.get_description() != "new":
            self.fail()

    def test_delete(self):
        event: Event = self.__test_repo.get_all()[0]
        used_sale = Sale(Person(1, "a", "a"), event)
        sales_repo = SaleRepo([used_sale])
        self.__test_repo.delete(event)
        if event in self.__test_repo.get_all():
            self.fail()
        try:
            self.__test_repo.delete(Event(0, datetime.datetime.today(), 1, "aaa"))
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()

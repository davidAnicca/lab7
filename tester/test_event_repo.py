import datetime
from unittest import TestCase

from domain.event import Event
from repo.event_repo import EventRepo
from repo.repo_error import RepoError


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

    def test_find_by_id(self):
        event: Event = self.__test_repo.get_all()[0]
        found_event = self.__test_repo.find_by_id(event.get_id())
        if found_event != event:
            self.fail()
        found_event = self.__test_repo.find_by_id(0)
        if found_event is not None:
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

    def test_modify_date(self):
        event: Event = self.__test_repo.get_all()[0]
        self.__test_repo.modify_date(event, datetime.datetime.today())
        if event.get_date() != datetime.datetime.today():
            self.fail()
        try:
            self.__test_repo.modify_date(Event(5, datetime.datetime.today(), 1, "aaa"),
                                         datetime.datetime.today())
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()

    def test_modify_duration(self):
        event: Event = self.__test_repo.get_all()[0]
        self.__test_repo.modify_duration(event, 3)
        if event.get_duration() != 3:
            self.fail()
        try:
            self.__test_repo.modify_duration(Event(5, datetime.datetime.today(), 1, "aaa"),
                                             3)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()

    def test_modify_descriprion(self):
        event: Event = self.__test_repo.get_all()[0]
        self.__test_repo.modify_description(event, "a")
        if event.get_description() != "a":
            self.fail()
        try:
            self.__test_repo.modify_description(Event(5, datetime.datetime.today(), 1, "aaa"),
                                                "a")
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()

    def test_delete(self):
        event: Event = self.__test_repo.get_all()[0]
        self.__test_repo.delete(event)
        if event in self.__test_repo.get_all():
            self.fail()
        try:
            self.__test_repo.delete(Event(5, datetime.datetime.today(), 1, "aaa"))
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()



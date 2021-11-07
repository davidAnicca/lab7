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

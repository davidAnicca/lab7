import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.dto.event_repo_dto import EventRepoDTO
from repo.event_repo import EventRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class TestEventRepo(TestCase):

    def setUp(self) -> None:
        file_path = "tester/events.csv"
        with open(file_path, "w") as f:
            f.write("")
            f.close()
        self.__test_repo = EventRepoDTO([Event(1, datetime.date.today(), 1, "description1"),
                                         Event(2, datetime.date.today(), 1, "lol"),
                                         Event(3, datetime.date.today(), 1, "macarena")], file_path)

    def tearDown(self) -> None:
        del self.__test_repo

    def test_find(self):
        event: Event = self.__test_repo.get_all()[0]
        self.assertEqual(event, self.__test_repo.find(event))
        event = Event(0, datetime.datetime.today(), 1, "nu ex")
        self.assertRaises(RepoError, self.__test_repo.find, event)

    def test_add(self):
        event = Event(5, datetime.datetime.today(), 1, "aaa")
        self.__test_repo.add(event)
        self.assertEqual(event, self.__test_repo.find(event))
        self.assertRaises(RepoError, self.__test_repo.add, self.__test_repo.get_all()[0])

    def test_modify(self):
        event = Event(0, datetime.date.today(), 2, "")
        self.assertRaises(RepoError, self.__test_repo.modify, event)
        new_event = Event(2, datetime.date.today() + datetime.timedelta(days=2), 2, "new")
        self.__test_repo.modify(new_event)
        modified: Event = self.__test_repo.find(new_event)
        self.assertEqual(modified.get_date(), new_event.get_date())
        self.assertEqual(modified.get_duration(), new_event.get_duration())
        self.assertEqual(modified.get_description(), new_event.get_description())

    def test_delete(self):
        event: Event = self.__test_repo.get_all()[0]
        self.__test_repo.delete(event)
        self.assertNotIn(event, self.__test_repo.get_all())
        self.assertRaises(RepoError, self.__test_repo.delete, Event(0, datetime.datetime.today(), 1, "aaa"))

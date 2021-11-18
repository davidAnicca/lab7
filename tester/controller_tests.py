import datetime
from unittest import TestCase

from controller.person_srv import PersonService
from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.event_repo import EventRepo
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class ControllerTest(TestCase):
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
        self.__test_person_srv = PersonService(self.__test_person_repo, self.__test_sale_repo)

    def test_create_person(self):
        p_id = 4
        p_name = "nume"
        p_address = "adresaa"
        obj = self.__test_person_srv.create_person(p_id, p_name, p_address)
        if not isinstance(obj, Person):
            self.fail()
        if obj.get_id() != p_id:
            self.fail()
        if obj.get_name() != p_name:
            self.fail()
        if obj.get_address() != p_address:
            self.fail()

    def test_add_person(self):

        p_id = 10
        p_name = "nume"
        p_address = "adresaa"
        try:
            self.__test_person_srv.add_person(1, p_name, p_address)
            self.fail()
        except RepoError as e:
            if str(e) != "id deja existent":
                self.fail()
        self.__test_person_srv.add_person(p_id, p_name, p_address)
        persons = self.__test_person_repo.get_all()
        for person in persons:
            if person.get_id() == p_id and \
                    person.get_name() == p_name and \
                    person.get_address() == p_address:
                return
        self.fail()

    def test_delete(self):
        try:
            self.__test_person_srv.delete_person(7)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()
        person = self.__test_person_repo.find_by_id(1)
        try:
            self.__test_person_srv.delete_person(1)
            persons = self.__test_person_repo.get_all()
            if person in persons:
                self.fail()
        except Exception:
            self.fail()

    def test_modify(self):
        try:
            self.__test_person_srv.modify_name(11, "name")
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

        try:
            self.__test_person_srv.modify_address(11, "address")
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

        try:
            self.__test_person_srv.modify_name(1, "name")
            self.__test_person_srv.modify_address(1, "address")
            person: Person = self.__test_person_repo.find_by_id(1)
            if person.get_name() != "name" or person.get_address() != "address":
                self.fail()
        except Exception:
            self.fail()

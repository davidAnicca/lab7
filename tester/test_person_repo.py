import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class TestPersonRepo(TestCase):

    def __init__(self):
        self.__test_repo = PersonRepo([Person(1, "maria", "cluj"),
                                       Person(2, "george", "turda"),
                                       Person(3, "cornel", "constanța")])

    def test_find(self):
        person = self.__test_repo.get_all()[0]
        try:
            self.__test_repo.find(person)
        except RepoError:
            self.fail()
        person = Person(0, "a", "a")
        try:
            self.__test_repo.find(person)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

    def test_find_by_id(self):
        person = self.__test_repo.find(Person(1, "maria", "c"))
        if person != self.__test_repo.get_all()[0]:
            self.fail()
        try:
            person = self.__test_repo.find(Person(0, "a", "a"))
            self.fail()
        except RepoError:
            pass

    def test_add(self):
        person_to_add = Person(4, "Ioan", "București")
        self.__test_repo.add(person_to_add)
        persons = self.__test_repo.get_all()
        if person_to_add not in persons:
            self.fail()
        person_to_add = Person(1, "Marcel", "Bacău")
        try:
            self.__test_repo.add(person_to_add)
            self.fail()
        except RepoError as e:
            if str(e) != "id deja existent":
                self.fail()

    def test_modify(self):
        person_to_be_modified: Person = self.__test_repo.get_all()[0]
        new_person = (Person(person_to_be_modified.get_id(), "marcel", "new address"))
        self.__test_repo.modify(new_person)
        person_to_be_modified: Person = self.__test_repo.get_all()[0]
        if person_to_be_modified.get_name() != "marcel":
            self.fail()
        if person_to_be_modified.get_address() != "new address":
            self.fail()
        person_to_be_modified: Person = Person("-7", "k", "k")
        try:
            self.__test_repo.modify(person_to_be_modified)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()


    def test_delete(self):
        person_to_be_deleted: Person = self.__test_repo.get_all()[0]
        used_sale = Sale(person_to_be_deleted, Event(1, datetime.date.today(), 1, "a"))
        sale_repo = SaleRepo([used_sale])
        self.__test_repo.delete(person_to_be_deleted, sale_repo)
        if person_to_be_deleted in self.__test_repo.get_all():
            self.fail()
        if used_sale in sale_repo.get_all():
            self.fail()
        person_to_be_deleted: Person = Person(-1, "a", "a")
        try:
            self.__test_repo.delete(person_to_be_deleted, sale_repo)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

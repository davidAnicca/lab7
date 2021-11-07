from unittest import TestCase

from domain.person import Person
from repo.person_repo import PersonRepo, RepoError


class TestPersonRepo(TestCase):

    def __init__(self):
        self.__test_repo = PersonRepo([Person(1, "maria", "cluj"),
                                       Person(2, "george", "turda"),
                                       Person(3, "cornel", "constanța")])

    def test_find_by_id(self):
        person = self.__test_repo.find_by_id(1)
        if person != self.__test_repo.get_all()[0]:
            self.fail()
        person = self.__test_repo.find_by_id(0)
        if person is not None:
            self.fail()

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

    def test_modify_name(self):
        person_to_be_modified: Person = self.__test_repo.get_all()[0]
        self.__test_repo.modify_name(person_to_be_modified, "marcel")
        if person_to_be_modified.get_name() != "marcel":
            self.fail()
        person_to_be_modified: Person = Person("-7", "k", "k")
        try:
            self.__test_repo.modify_name(person_to_be_modified, "a")
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

    def test_modify_address(self):
        person_to_be_modified: Person = self.__test_repo.get_all()[0]
        self.__test_repo.modify_address(person_to_be_modified, "new address")
        if person_to_be_modified.get_address() != "new address":
            self.fail()
        person_to_be_modified: Person = Person("-7", "k", "k")
        try:
            self.__test_repo.modify_address(person_to_be_modified, "a")
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

    def test_delete(self):
        person_to_be_deleted : Person = self.__test_repo.get_all()[0]
        self.__test_repo.delete(person_to_be_deleted)
        if person_to_be_deleted in self.__test_repo.get_all():
            self.fail()
        person_to_be_deleted : Person = Person(-1, "a", "a")
        try:
            self.__test_repo.delete(person_to_be_deleted)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()


import datetime
from unittest import TestCase

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.dto.person_repo_dto import PersonRepoDTO
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class TestPersonRepo(TestCase):

    def setUp(self) -> None:
        path = "tester/persons.csv"
        with open(path, "w") as f:
            f.write("")
            f.close()
        self.__test_repo = PersonRepoDTO([Person(1, "maria", "cluj"),
                                          Person(2, "george", "turda"),
                                          Person(3, "cornel", "constanta")], path)

    def tearDown(self) -> None:
        del self.__test_repo

    def test_find(self):
        person = self.__test_repo.get_all()[0]
        self.assertRaises(RepoError, self.__test_repo.find, Person(0, "a", "a"))

    def test_find_by_id(self):
        person = self.__test_repo.find(Person(1, "maria", "c"))
        self.assertEqual(person, self.__test_repo.get_all()[0])
        self.assertRaises(RepoError, self.__test_repo.find, Person(0, "a", "a"))

    def test_add(self):
        person_to_add = Person(4, "Ioan", "Bucuresti")
        self.__test_repo.add(person_to_add)
        persons = self.__test_repo.get_all()
        self.assertIn(person_to_add, persons)
        person_to_add = Person(1, "Marcel", "Bacau")
        self.assertRaises(RepoError, self.__test_repo.add, person_to_add)

    def test_modify(self):
        person_to_be_modified: Person = self.__test_repo.get_all()[0]
        new_person = (Person(person_to_be_modified.get_id(), "marcel", "new address"))
        self.__test_repo.modify(new_person)
        person_to_be_modified: Person = self.__test_repo.find(new_person)
        self.assertEqual(person_to_be_modified.get_name(), "marcel")
        self.assertEqual(person_to_be_modified.get_address(), "new address")
        person_to_be_modified: Person = Person("-7", "k", "k")
        self.assertRaises(RepoError, self.__test_repo.modify, person_to_be_modified)

    def test_delete(self):
        person_to_be_deleted: Person = self.__test_repo.get_all()[0]
        self.__test_repo.delete(person_to_be_deleted)
        self.assertNotIn(person_to_be_deleted, self.__test_repo.get_all())
        person_to_be_deleted: Person = Person(-1, "a", "a")
        self.assertRaises(RepoError, self.__test_repo.delete, person_to_be_deleted)

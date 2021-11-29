import csv

from domain.person import Person
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


class PersonRepoDTO(PersonRepo):

    def __init__(self, persons: list, file_path):
        PersonRepo.__init__(self, persons)
        self.__path = file_path
        for person in persons:
            self.append_one(person)
        self.__read_all()

    def __read_all(self):
        self._persons = []
        with open(self.__path, "r") as f:
            line = f.readline()
            while line != "":
                parts = line.split(',')
                person = Person(int(parts[0]), parts[1], parts[2])
                self._persons.append(person)
                line = f.readline()
            f.close()

    def save_all(self):
        with open(self.__path, "w") as f:
            for person in self._persons:
                f.write(f"{str(person.get_id())},{person.get_name()},{person.get_address()},\n")
            f.close()

    def append_one(self, person: Person):
        with open(self.__path, "a") as f:
            f.write(f"{str(person.get_id())},{person.get_name()},{person.get_address()},\n")
            f.close()

    def get_all(self):
        self.__read_all()
        return PersonRepo.get_all(self)

    def find(self, person: Person):
        self.__read_all()
        return PersonRepo.find(self, person)

    def add(self, person: Person):
        self.__read_all()
        PersonRepo.add(self, person)
        self.append_one(person)

    def modify(self, person):
        self.__read_all()
        PersonRepo.modify(self, person)
        self.save_all()

    def delete(self, person: Person):
        self.__read_all()
        PersonRepo.delete(self, person)
        self.save_all()

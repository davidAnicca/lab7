from domain.person import Person
from repo.repo_error import RepoError


class PersonRepo(object):

    def __init__(self, persons):
        self.__persons: list = persons

    def get_all(self):
        return self.__persons

    def find(self, person):
        if person not in self.__persons:
            del person
            raise RepoError("persoana nu exista")

    def find_by_id(self, p_id):
        for person in self.__persons:
            if person.get_id() == p_id:
                return person
        return None

    def add(self, person: Person):
        if self.find_by_id(person.get_id()) is not None:
            del person
            raise RepoError("id deja existent")
        self.__persons.append(person)

    def modify_name(self, person: Person, name):
        self.find(person)
        person.set_name(name)

    def modify_address(self, person: Person, address):
        self.find(person)
        person.set_address(address)

    def delete(self, person: Person):
        self.find(person)
        self.__persons.remove(person)
        del person

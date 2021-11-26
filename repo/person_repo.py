from domain.person import Person
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class PersonRepo(object):
    """
    repository class that retains a list of person objects and performs CRUD operation on it
    it only works with existent objects.
    able to delete invalid objects
    """

    def __init__(self, persons: list):
        self.__persons: list = persons

    # returns all persons from self. repo
    def get_all(self):
        return self.__persons

    def find(self, person: Person):
        """
        checks if a person is in repo or not
        :returns that person if can find it
        :raises: RepoError if the person cannot be found
        """
        persons = self.get_all()
        for p in persons:
            if p == person:
                return p
        raise RepoError("persoana nu exista")

    def add(self, person: Person):
        """
        adds a person  in repo
        :param person: person to be added
        :raises: RepoError if given person has an id that already exist in repo
        """
        try:
            self.find(person)
        except RepoError:
            self.__persons.append(person)
            return
        raise RepoError("id deja existent")

    def modify(self, person):
        """
        changes the person from repo with an id with another instance
        :param person: new person to be changed
        :raises: RepoError if person cannot be found
        """
        old_person = self.find(person)
        self.__persons.remove(old_person)
        self.__persons.append(person)
        old_person = person

    def delete(self, person: Person):
        """
        deletes a person from repo and all sales of it
        :param person: event to be deleted
        :raises: RepoError if person doesn't exist
        """
        self.find(person)
        self.__persons.remove(person)
        del person

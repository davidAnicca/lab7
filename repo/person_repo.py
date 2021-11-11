from domain.person import Person
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class PersonRepo(object):
    """
    repository class that retains a list of person objects and performs CRUD operation on it
    it only works with existent objects.
    able to delete invalid objects
    """

    def __init__(self, persons):
        self.__persons: list = persons

    # returns all persons from self. repo
    def get_all(self):
        return self.__persons

    def find(self, person):
        """
        checks if a person exist or not in self repository.
        it deletes the person object if it doesn't exist
        :param person: person object
        :return: -
        :raises: RepoError if the person doesn't exist.
        """
        if person not in self.__persons:
            del person
            raise RepoError("persoana nu exista")

    def find_by_id(self, p_id):
        """
        checks if an person-id exist or not in self repo
        :param p_id: id to be found
        :return: an person object with given id or None if doesn't exist
        """
        for person in self.__persons:
            if person.get_id() == p_id:
                return person
        return None

    def add(self, person: Person):
        """
        adds a person  in repo
        :param person: person to be added
        :raises: RepoError if given person has an id that already exist in repo
        """
        if self.find_by_id(person.get_id()) is not None:
            del person
            raise RepoError("id deja existent")
        self.__persons.append(person)

    def modify_name(self, person: Person, name):
        """
        modifies name for a person
        :param person: person to be modified
        :param name: new name to be changed
        :raises: RepoError if person doesn't exist
        """
        self.find(person)
        person.set_name(name)

    def modify_address(self, person: Person, address):
        """
        modifies address for a person
        :param person: person to be modified
        :param address: new address to be changed
        :raises: RepoError if person doesn't exist
        """
        self.find(person)
        person.set_address(address)

    def delete(self, person: Person, sale_repo: SaleRepo):
        """
        deletes a person from repo and all sales of it
        :param sale_repo: sale repo
        :param person: event to be deleted
        :raises: RepoError if person doesn't exist
        """
        self.find(person)
        self.__persons.remove(person)
        sales = sale_repo.find_by__person(person)
        for sale in sales:
            sale_repo.delete(sale)
        del person

from domain.person import Person
from logic.person_logic import PersonLogic
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class PersonService(object):
    def __init__(self, person_repo: PersonRepo, sale_repo: SaleRepo):
        self.__person_repo = person_repo
        self.__sale_repo = sale_repo

    def create_person(self, p_id: int, p_name, p_address):
        """
        base on some credentials, it creates a person
        :param p_id: id of person
        :param p_name: name of person
        :param p_address: address of person
        :return: a logically-valid Person object
        """
        return Person(p_id, p_name, p_address)

    def add_person(self, p_id: int, p_name, p_address):
        """
        adds a person in repo after it creates it
        :param p_id: id of person
        :param p_name: name
        :param p_address: address
        :raises: RepoError if the person couldn't be added to repo
        """
        person = self.create_person(p_id, p_name, p_address)
        try:
            self.__person_repo.add(person)
        except RepoError as e:
            raise e

    def delete_person(self, p_id: int):
        """
        Deletes a person from repo, based on id
        :param p_id: id
        :raises: RepoError if the person cannot be found
        """
        try:
            person = self.__person_repo.find(Person(p_id, "a", "a"))
            if person is None:
                raise RepoError("persoana nu exista")
            self.__person_repo.delete(person)
            sales_to_delete = []
            sales = self.__sale_repo.get_all()
            for sale in sales:
                if sale.get_person() == person:
                    sales_to_delete.append(sale)
            for sale in sales_to_delete:
                self.__sale_repo.delete(sale)
        except RepoError as e:
            raise e

    def get_all(self):
        """
        returns all the list from repo
        :return:
        """
        return self.__person_repo.get_all()

    def modify_name(self, p_id: int, p_name):
        """
        modifies the name based on id
        :param p_id: id to be modified
        :param p_name: new name
        :raises: RepoError if the person cannot be found
        """
        try:
            person = self.__person_repo.find(Person(p_id, "a", "a"))
            new_person = Person(p_id, p_name, person.get_address())
            self.__person_repo.modify(new_person)
        except RepoError as e:
            raise e

    def modify_address(self, p_id, p_address):
        """
        modifies the address based on id
        :param p_id: id to be modified
        :param p_address: new address
        :raises: RepoError if the person cannot be found
        """
        try:
            person = self.__person_repo.find(Person(p_id, "a", "a"))
            new_person = Person(p_id, person.get_name(), p_address)
            self.__person_repo.modify(new_person)
        except RepoError as e:
            raise e

    def get_active(self):
        logic = PersonLogic(self.__person_repo, self.__sale_repo)
        return logic.get_person_with_most_events()

    def events_date(self, p_id):
        """
        returns events ordered by date for a person
        :param p_id: person id
        :raises: RepoError if the person cannot be found
        """
        person = self.__person_repo.find(Person(p_id, "a", "a"))
        logic = PersonLogic(self.__person_repo, self.__sale_repo)
        return logic.get_all_my_events_ordered_by_date(person)

    def events_desc(self, p_id):
        """
             returns events ordered by duration for a person
             :param p_id: person id
             :raises: RepoError if the person cannot be found
             """
        person = self.__person_repo.find(Person(p_id, "a", "a"))
        logic = PersonLogic(self.__person_repo, self.__sale_repo)
        return logic.get_all_my_events_ordered_by_duration(person)


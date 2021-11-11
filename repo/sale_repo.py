from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.repo_error import RepoError


class SaleRepo(object):

    def __init__(self, sales: list):
        self.__sales = sales

    # returns all sales from repo
    def get_all(self):
        return self.__sales

    def assert_exist(self, sale):
        """
        checks if a sale exist in repo
        :param sale: given sale
        :raises: repo error if sale doesn't exist
        """
        if sale not in self.__sales:
            del sale
            raise RepoError("participarea nu există")

    def find_by__person(self, person):
        """
        returns all sales that contain a person
        :param person: given person
        :return: a list
        """
        sales = []
        for sale in self.__sales:
            if sale.get_person() == person:
                sales.append(sale)
        return sales

    def find_by_event(self, event):
        """
        return all sales that contain an event
        :param event: given event
        :return: a list
        """
        sales = []
        for sale in self.__sales:
            if sale.get_event() == event:
                sales.append(sale)
        return sales

    def find_by_pair(self, person: Person, event: Event):
        """
        search for a sale in repo using pair params
        :param person: person param
        :param event: event param
        :return: found sale or None if sale cannot be found
        """
        for sale in self.__sales:
            if sale.get_person() == person and sale.get_event() == event:
                return sale
        return None

    def add(self, sale: Sale):
        """
        adds a sale in repo
        :param sale: given sale
        :raises: RepoError if the sale already exist in repo
        """
        if self.find_by_pair(sale.get_person(), sale.get_event()) is not None:
            del sale
            raise RepoError("participarea deja există")
        self.__sales.append(sale)

    def delete(self, sale: Sale):
        """
        deletes a sale from repo
        :param sale: sale to be deleted
        :raise: RepoError if the sale doesn't exist
        """
        self.assert_exist(sale)
        self.__sales.remove(sale)
        del sale

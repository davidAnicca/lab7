from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.repo_error import RepoError


class SaleRepo(object):

    def __init__(self, sales: list):
        self._sales = sales

    # returns all sales from repo
    def get_all(self):
        return self._sales

    def assert_exist(self, sale):
        """
        checks if a sale exist in repo
        :param sale: given sale
        :raises: repo error if sale doesn't exist
        """
        if sale not in self._sales:
            del sale
            raise RepoError("participarea nu există")


    def find_by_pair(self, person: Person, event: Event):
        """
        search for a sale in repo using pair params
        :param person: person param
        :param event: event param
        :return: found sale or None if sale cannot be found
        """
        for sale in self._sales:
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
        self._sales.append(sale)

    def delete(self, sale: Sale):
        """
        deletes a sale from repo
        :param sale: sale to be deleted
        :raise: RepoError if the sale doesn't exist
        """
        self.assert_exist(sale)
        self._sales.remove(sale)
        del sale

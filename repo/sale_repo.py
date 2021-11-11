from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.repo_error import RepoError


class SaleRepo(object):

    def __init__(self, sales: list):
        self.__sales = sales

    def get_all(self):
        return self.__sales

    def find(self, sale):
        if sale not in self.__sales:
            del sale
            raise RepoError("participarea nu există")

    def find_by_pair(self, person: Person, event: Event):
        for sale in self.__sales:
            if sale.get_person() == person and sale.get_event() == event:
                return sale
        return None

    def add(self, sale: Sale):
        if self.find_by_pair(sale.get_person(), sale.get_event()):
            del sale
            raise RepoError("participarea deja există")
        self.__sales.append(sale)

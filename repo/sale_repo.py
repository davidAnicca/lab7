from domain.event import Event
from domain.person import Person
from repo.repo_error import RepoError


class SaleRepo(object):

    def __init__(self, sales: list):
        self.__sales = sales

    def get_all(self):
        return self.__sales

    def find(self, sale):
        if sale in self.__sales:
            del sale
            raise RepoError("participarea deja există")

    def find_by_pair(self, person: Person, event: Event):
        pass



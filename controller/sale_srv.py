from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.event_repo import EventRepo
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class SaleService(object):
    def __init__(self, person_repo: PersonRepo, event_repo: EventRepo, sale_repo: SaleRepo):
        self.__person_repo = person_repo
        self.__event_repo = event_repo
        self.__sale_repo = sale_repo

    def create_sale(self, p_id, e_id):
        """
        creates a sale object based on person id and event id
        :param p_id: p id
        :param e_id: e id
        :raises: RepoError if event or person cannot be found or both
        """
        person = self.__person_repo.find(Person(p_id, "a", "a"))
        if person is None:
            raise RepoError("persoana nu exista")
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        if event is None:
            raise RepoError("evenimentul nu exista")
        return Sale(person, event)

    def add_sale(self, p_id, e_id):
        """
        adds a sale in list based on id for person or event
        :param p_id: p id
        :param e_id: e id
        :raises: RepoError if person or event cannot be found. Also RepoError if the sale is already in repo
        """
        person = self.__person_repo.find(Person(p_id, "a", "a"))
        if person is None:
            raise RepoError("persoana nu exista")
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        if event is None:
            raise RepoError("evenimentul nu exista")
        self.__sale_repo.add(Sale(person, event))

    def delete_sale(self, p_id, e_id):
        """
        deletes the sale that contain person with p_id and event with e_id :param p_id: :param e_id: :raises:
        RepoError if person/event cannot be found. RepoError if doesn't exist a sale with given person and event
        """
        person = self.__person_repo.find(Person(p_id, "a", "a"))
        if person is None:
            raise RepoError("persoana nu exista")
        event = self.__event_repo.find(Event(e_id, None, 0, ""))
        if event is None:
            raise RepoError("evenimentul nu exista")
        sale = self.__sale_repo.find_by_pair(person, event)
        if sale is None:
            raise RepoError("participarea nu exist??")
        self.__sale_repo.delete(sale)

    def get_all(self):
        return self.__sale_repo.get_all()

    def possible_size(self):
        # computes the possible sale number to generate
        return len(self.__person_repo.get_all())*len(self.__event_repo.get_all())

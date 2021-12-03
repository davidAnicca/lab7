import datetime

from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.dto.event_repo_dto import EventRepoDTO
from repo.dto.person_repo_dto import PersonRepoDTO
from repo.sale_repo import SaleRepo


class SaleRepoDTO(SaleRepo):

    def __init__(self, sales: list, person_repo: PersonRepoDTO, event_repo: EventRepoDTO, file_path):
        self.__person_repo = person_repo
        self.__event_repo = event_repo
        self.__file_path = file_path
        SaleRepo.__init__(self, sales)
        for sale in sales:
            self.append_one(sale)
        self.read_all()

    def read_all(self):
        self._sales = []
        with open(self.__file_path, 'r') as f:
            first = f.readline()
            second = f.readline()
            while first != '' or second != '':
                p_id = int(first.strip())
                e_id = int(second.strip())
                person = self.__person_repo.find(Person(p_id, '', ''))
                event = self.__event_repo.find(Event(e_id, datetime.datetime.now(), 0, ''))
                self._sales.append(Sale(person, event))
                first = f.readline()
                second = f.readline()
            # line = f.readline()
            # self._sales = []
            # while line != "":
            #     parts = line.split(',')
            #     p_id = int(parts[0])
            #     e_id = int(parts[1])
            #     person = self.__person_repo.find(Person(p_id, '', ''))
            #     event = self.__event_repo.find(Event(e_id, datetime.datetime.now(), 0, ''))
            #     self._sales.append(Sale(person, event))
            #     line = f.readline()
            f.close()

    def save_all(self):
        with open(self.__file_path, 'w') as f:
            for sale in self._sales:
                f.write(str(sale.get_person().get_id()) + '\n')
                f.write(str(sale.get_event().get_id()) + '\n')
            f.close()

    def append_one(self, sale: Sale):
        with open(self.__file_path, 'a') as f:
            f.write(str(sale.get_person().get_id()) + '\n')
            f.write(str(sale.get_event().get_id()) + '\n')
            f.close()

    def get_all(self):
        self.read_all()
        return SaleRepo.get_all(self)

    def assert_exist(self, sale):
        self.read_all()
        return SaleRepo.assert_exist(self, sale)

    def find_by_pair(self, person: Person, event: Event):
        self.read_all()
        return SaleRepo.find_by_pair(self, person, event)

    def add(self, sale: Sale):
        self.read_all()
        SaleRepo.add(self, sale)
        self.append_one(sale)

    def delete(self, sale: Sale):
        self.read_all()
        SaleRepo.delete(self, sale)
        self.save_all()

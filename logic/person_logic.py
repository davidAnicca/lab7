from domain.person import Person
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


class PersonLogic(object):
    def __init__(self, person_repo: PersonRepo, sale_repo: SaleRepo):
        self.__sale_repo = sale_repo
        self.__person_repo = person_repo

    def get_person_with_most_events(self):
        """
        identifies the person with the biggest num of participation
        :return: person object (first identified)
        """
        persons = self.__person_repo.get_all()
        sales = self.__sale_repo.get_all()
        max_num = None
        identified = None
        for person in persons:
            num = 0
            for sale in sales:
                if sale.get_person() == person:
                    num+=1
            if max_num is None or num > max_num:
                max_num = num
                identified = person
        return identified

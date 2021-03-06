from domain.event import Event
from domain.person import Person
from logic import sorting
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


def duration(event: Event):
    return event.get_duration()


class PersonLogic(object):
    def __init__(self, person_repo: PersonRepo, sale_repo: SaleRepo):
        self.__sale_repo = sale_repo
        self.__person_repo = person_repo

    def get_person_with_most_events(self):
        """
        identifies the person with the biggest num of participation
        :return: a list of persons. Empty if empty
        """
        persons = self.__person_repo.get_all()
        sales = self.__sale_repo.get_all()
        max_num = None
        identified = []
        for person in persons:
            num = 0
            for sale in sales:
                if sale.get_person() == person:
                    num += 1
            if max_num is None or num > max_num:
                max_num = num

        for person in persons:
            num = 0
            for sale in sales:
                if sale.get_person() == person:
                    num += 1
            if max_num is None or num == max_num:
                identified.append(person)
        return identified

    def get_all_my_events_ordered_by_date(self, person: Person):
        """
        for a person, returns all events sorted by date
        :param person: given person
        :return: a list of events (sorted)
        """
        sales = self.__sale_repo.get_all()
        events = []
        for sale in sales:
            if sale.get_person() == person:
                events.append(sale.get_event())
        sorting.sort(events, keyy=lambda e: e.get_date())
        # events.sort(key=lambda e: e.get_date())
        return events

    def get_all_my_events_ordered_by_duration(self, person: Person):
        """
                for a person, returns all events sorted by description
                :param person: given person
                :return: a list of events (sorted)
                """
        sales = self.__sale_repo.get_all()
        events = []
        for sale in sales:
            if sale.get_person() == person:
                events.append(sale.get_event())
        sorting.sort(events, keyy=lambda e: e.get_description())
        # events.sort(key=lambda e: e.get_description())
        return events

from domain.event import Event
from domain.person import Person


class Sale(object):

    def __init__(self, person: Person, event: Event):
        self.__person = person
        self.__event = event

    def get_person(self):
        return self.__person

    def get_event(self):
        return self.__event

    def set_person(self, person: Person):
        self.__person = person

    def set_event(self, event: Event):
        self.__event = event

    def __str__(self):
        return str(self.__person) + " " + str(self.__event)






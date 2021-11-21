import datetime
from unittest import TestCase

from controller.event_srv import EventService
from controller.person_srv import PersonService
from controller.sale_srv import SaleService
from domain.event import Event
from domain.person import Person
from domain.sale import Sale
from repo.event_repo import EventRepo
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo
from validation.event_validator import EventValidator
from validation.validation_error import ValidationError


class ControllerTest(TestCase):
    def __init__(self):
        self.__test_events_repo = EventRepo([Event(0, datetime.date.today(), 1, "a"),
                                             Event(1, datetime.date.today() + datetime.timedelta(days=20), 6, "c"),  #del
                                             Event(2, datetime.date.today() + datetime.timedelta(days=10), 1, "b"),
                                             Event(3, datetime.date.today() + datetime.timedelta(days=10), 1, "b")])
        self.__test_person_repo = PersonRepo([Person(0, "marcel", "cluj"),
                                              Person(1, "cristian", "turda"),  #del
                                              Person(2, "maria", "cluj"),
                                              Person(3, "ionel", "cluj")])
        self.__test_sale_repo = SaleRepo([Sale(self.__test_person_repo.get_all()[0],  # 0 2
                                               self.__test_events_repo.get_all()[2]),
                                          Sale(self.__test_person_repo.get_all()[1],  # 1 2
                                               self.__test_events_repo.get_all()[2]),
                                          Sale(self.__test_person_repo.get_all()[1],  # 1 0
                                               self.__test_events_repo.get_all()[0]),
                                          Sale(self.__test_person_repo.get_all()[1],  # 1 1
                                               self.__test_events_repo.get_all()[1]),
                                          Sale(self.__test_person_repo.get_all()[2],  # 2 2
                                               self.__test_events_repo.get_all()[2]),
                                          ])
        self.__test_person_srv = PersonService(self.__test_person_repo, self.__test_sale_repo)
        self.__test_event_srv = EventService(self.__test_events_repo, self.__test_sale_repo)
        self.__test_sale_srv = SaleService(self.__test_person_repo, self.__test_events_repo, self.__test_sale_repo)

    def test_create_person(self):
        p_id = 4
        p_name = "nume"
        p_address = "adresaa"
        obj = self.__test_person_srv.create_person(p_id, p_name, p_address)
        if not isinstance(obj, Person):
            self.fail()
        if obj.get_id() != p_id:
            self.fail()
        if obj.get_name() != p_name:
            self.fail()
        if obj.get_address() != p_address:
            self.fail()

    def test_add_person(self):

        p_id = 10
        p_name = "nume"
        p_address = "adresaa"
        try:
            self.__test_person_srv.add_person(1, p_name, p_address)
            self.fail()
        except RepoError as e:
            if str(e) != "id deja existent":
                self.fail()
        self.__test_person_srv.add_person(p_id, p_name, p_address)
        persons = self.__test_person_repo.get_all()
        for person in persons:
            if person.get_id() == p_id and \
                    person.get_name() == p_name and \
                    person.get_address() == p_address:
                return
        self.fail()

    def test_delete(self):
        try:
            self.__test_person_srv.delete_person(7)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

        self.__test_person_srv.delete_person(1)
        persons = self.__test_person_repo.get_all()
        for person in persons:
            if person.get_id() == 1:
                self.fail()


    def test_modify(self):
        try:
            self.__test_person_srv.modify_name(11, "name")
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

        try:
            self.__test_person_srv.modify_address(11, "address")
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()

        try:
            self.__test_person_srv.modify_name(1, "name")
            self.__test_person_srv.modify_address(1, "address")
            person: Person = self.__test_person_repo.find(Person(1, "a", "a"))
            if person.get_name() != "name" or person.get_address() != "address":
                self.fail()
        except Exception:
            self.fail()

    def test_create_event(self):
        e_id = 10
        e_date = datetime.date.today() - datetime.timedelta(days=10)
        e_duration = 3
        e_description = "descriere"
        try:
            self.__test_event_srv.create_event(e_id, e_date, e_duration, e_description)
            self.fail()
        except ValidationError as e:
            if str(e) != "nu se poate crea un eveniment în trecut":
                self.fail()
        e_date = e_date + datetime.timedelta(days=11)
        obj = self.__test_event_srv.create_event(e_id, e_date, e_duration, e_description)
        if not isinstance(obj, Event):
            self.fail()
        if obj.get_id() != e_id or \
                obj.get_date() != e_date or \
                obj.get_duration() != e_duration or \
                obj.get_description() != e_description:
            self.fail()

    def test_add_event(self):
        e_id = 10
        e_date = datetime.date.today()
        e_duration = 3
        e_description = "desc"
        try:
            self.__test_event_srv.add_event(1,
                                            datetime.date.today() + datetime.timedelta(days=10),
                                            e_duration,
                                            e_description)
            self.fail()
        except RepoError as e:
            if str(e) != "id deja existent":
                self.fail()
        try:
            self.__test_event_srv.add_event(1, datetime.date.today() - datetime.timedelta(days=10),
                                            e_duration,
                                            e_description)
        except ValidationError as e:
            if str(e) != "nu se poate crea un eveniment în trecut":
                self.fail()
        self.__test_event_srv.add_event(e_id, e_date + datetime.timedelta(days=10), e_duration, e_description)
        events = self.__test_events_repo.get_all()
        for event in events:
            if event.get_id() == e_id and \
                    event.get_date() == e_date + datetime.timedelta(days=10) and \
                    event.get_duration() == e_duration and \
                    event.get_description() == e_description:
                return
        self.fail()

    def test_delete_event(self):
        try:
            self.__test_event_srv.delete_event(9)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()

        self.__test_event_srv.delete_event(1)
        events = self.__test_events_repo.get_all()
        for event in events:
            if event.get_id() == 1:
                self.fail()

    def test_modify_event(self):
        try:
            self.__test_event_srv.modify_date(20, datetime.date.today() + datetime.timedelta(days=10))
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()
        try:
            self.__test_event_srv.modify_duration(20, 2)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()
        try:
            self.__test_event_srv.modify_description(20, "aaaaaa")
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()

        try:
            self.__test_event_srv.modify_date(2, datetime.date.today() - datetime.timedelta(days=10))
            self.fail()
        except ValidationError as e:
            if str(e) != "nu se poate crea un eveniment în trecut":
                self.fail()
        self.__test_event_srv.modify_date(2, datetime.date.today() + datetime.timedelta(days=10))
        self.__test_event_srv.modify_duration(2, 3)
        self.__test_event_srv.modify_description(2, "blabla")
        modified: Event = self.__test_events_repo.find(Event(2, None, 0, ""))
        if modified.get_date() != datetime.date.today() + datetime.timedelta(days=10) or \
                modified.get_duration() != 3 or \
                modified.get_description() != "blabla":
            self.fail()

    def test_create_sale(self):
        try:
            self.__test_sale_srv.create_sale(22, 1)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()
        try:
            self.__test_sale_srv.create_sale(3, 22)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()
        sale: Sale = self.__test_sale_srv.create_sale(2, 2)
        if sale.get_person() != self.__test_person_repo.find(Person(2, "a", "a")):
            self.fail()
        if sale.get_event() != self.__test_events_repo.find(Event(2, None, 0, "")):
            self.fail()

    def test_add_sale(self):
        try:
            self.__test_sale_srv.add_sale(22, 1)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()
        try:
            self.__test_sale_srv.add_sale(3, 22)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()
        try:
            self.__test_sale_srv.add_sale(2, 2)
            self.fail()
        except RepoError as e:
            if str(e) != "participarea deja există":
                self.fail()
        self.__test_sale_srv.add_sale(2, 0)
        sales = self.__test_sale_repo.get_all()
        for sale in sales:
            if sale.get_person() == self.__test_person_repo.find(Person(2, "a", "a")) and \
                    sale.get_event() == self.__test_events_repo.find(Event(0, None, 0, "")):
                return
        self.fail()

    def test_delete_sale(self):
        try:
            self.__test_sale_srv.create_sale(22, 1)
            self.fail()
        except RepoError as e:
            if str(e) != "persoana nu exista":
                self.fail()
        try:
            self.__test_sale_srv.create_sale(3, 22)
            self.fail()
        except RepoError as e:
            if str(e) != "evenimentul nu exista":
                self.fail()
        try:
            self.__test_sale_srv.delete_sale(2, 3)
            self.fail()
        except RepoError as e:
            if str(e) != "participarea nu există":
                self.fail()
        self.__test_sale_srv.delete_sale(2, 0)
        sales = self.__test_sale_repo.get_all()
        for sale in sales:
            if sale.get_person() == self.__test_person_repo.find(Person(2, "a", "a")) and \
                    sale.get_event() == self.__test_events_repo.find(Event(0, None, 0, "")):
                self.fail()

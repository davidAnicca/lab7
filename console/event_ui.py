import datetime

from console.command_error import CommandError
from console.strings import strings
from controller.event_srv import EventService
from controller.random_generator import RandomGen


class EventUi(object):
    def __init__(self, event_service: EventService):
        self.__event_service = event_service

    def printer(self, collection):
        for element in collection:
            print(str(element))

    #top3
    def top3(self, command):
        self.printer(self.__event_service.first_3_events())

    # e
    def show_all(self, command):
        events = self.__event_service.get_all()
        self.printer(events)

    # rp [number]
    def random(self, command):
        if len(command.split()) > 2:
            raise CommandError(strings["re"])
        number = 1
        if len(command.split()) == 2:
            number = int(command.split()[1])
        rand = RandomGen(self.__event_service)
        rand.generate_events(number)

    # adde [id] [data] [durata] [descriere]
    def add(self, command):
        params = command.split()
        if len(params) < 4:
            raise CommandError(strings["adde"])
        desc = ""
        if len(params) >= 5:
            for param in params[4:]:
                desc += param + " "

        try:
            e_date = datetime.datetime.strptime(params[2], '%d/%m/%Y')
            try:
                self.__event_service.add_event(int(params[1]),
                                               datetime.date(e_date.year, e_date.month, e_date.day),
                                               int(params[3]),
                                               desc)
            except ValueError:
                print("valoare numerică invalidă pentru [id]")
        except ValueError:
            print(strings["adde"])

    # emd [id] [data dd/ll/aaaa]
    def mod_d(self, command):
        params = command.split()
        if len(params) != 3:
            raise CommandError(strings["emd"])
        try:
            e_date = datetime.datetime.strptime(params[2], '%d/%m/%Y')
            try:
                self.__event_service.modify_date(int(params[1]),
                                                 datetime.date(e_date.year, e_date.month, e_date.day))
            except ValueError:
                print("valoare numerică invalidă pentru [id]")
        except ValueError:
            print(strings["adde"])

    # emdr [id] [noua durata]
    def mod_dr(self, command):
        params = command.split()
        if len(params) != 3:
            raise CommandError(strings["emdr"])
        self.__event_service.modify_duration(int(params[1]), int(params[2]))

    # emde [id] [descriere noua]
    def mod_de(self, command):
        params = command.split()
        if len(params) < 2:
            raise CommandError(strings["emde"])
        desc = ""
        for word in params[2:]:
            desc += word + " "
        self.__event_service.modify_description(int(params[1]), desc)

    # edel [id]
    def delete(self, command):
        params = command.split()
        if len(params) != 2:
            raise CommandError(strings["edel"])
        self.__event_service.delete_event(int(params[1]))

    # soldouts
    def soldouts(self, command):
        self.printer(self.__event_service.soldouts())

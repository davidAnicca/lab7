import datetime

from console.command_error import CommandError
from console.strings import strings
from controller.event_srv import EventService
from controller.random_generator import RandomGen


class EventUi(object):
    def __init__(self, event_service: EventService):
        self.__event_service = event_service

    # e
    def show_all(self, command):
        events = self.__event_service.get_all()
        for event in events:
            print(event)

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
                print("nu se poate transforma")
        except ValueError:
            print(strings["adde"])

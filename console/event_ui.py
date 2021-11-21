from controller.event_srv import EventService
from controller.random_generator import RandomGen


class EventUi(object):
    def __init__(self, event_service: EventService):
        self.__event_service = event_service

    def show_all(self, command):
        events = self.__event_service.get_all()
        for event in events:
            print(event)

    def random(self, command):
        rand = RandomGen(self.__event_service)
        rand.generate_events(int(command.split()[1]))

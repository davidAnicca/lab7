from datetime import datetime

from domain.event import Event
from repo.event_repo import EventRepo


class EventRepoDTO(EventRepo):
    def __init__(self, events: list, path):
        EventRepo.__init__(self, events)
        self.__path = path
        self.save_all()

    def read_all(self):
        self._events = []
        with open(self.__path, "r") as f:
            line = f.readline()
            while line != "":
                info = line.split(',')
                # %d/%m/%y
                e_date = datetime.date(datetime.strptime(info[1], "%d/%m/%y"))
                event = Event(int(info[0]), e_date, int(info[2]), info[3].strip())
                self._events.append(event)
                line = f.readline()
            f.close()

    def save_all(self):
        with open(self.__path, "w") as f:
            for event in self._events:
                date_str = datetime.strftime(event.get_date(), "%d/%m/%y")
                f.write(
                    f"{str(event.get_id())},{date_str},{str(event.get_duration())},{str(event.get_description())},\n")
            f.close()

    def append_one(self, event: Event):
        with open(self.__path, "a") as f:
            date_str = datetime.strftime(event.get_date(), "%d/%m/%y")
            f.write(f"{str(event.get_id())},{date_str},{str(event.get_duration())},{str(event.get_description())},\n")

    def get_all(self):
        self.read_all()
        return EventRepo.get_all(self)

    def find(self, event: Event):
        self.read_all()
        return EventRepo.find(self, event)

    def add(self, event):
        self.read_all()
        EventRepo.add(self, event)
        self.append_one(event)

    def modify(self, event):
        self.read_all()
        EventRepo.modify(self, event)
        self.save_all()

    def delete(self, event):
        self.read_all()
        EventRepo.delete(self, event)
        self.save_all()

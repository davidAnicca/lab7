import datetime

from domain.event import Event
from repo.repo_error import RepoError


class EventRepo(object):

    def __init__(self, events: list):
        self.__events = events

    def get_all(self):
        return self.__events

    def find(self, event):
        if event not in self.__events:
            del event
            raise RepoError("evenimentul nu exista")

    def find_by_id(self, e_id):
        for event in self.__events:
            if event.get_id() == e_id:
                return event
        return None

    def add(self, event):
        if self.find_by_id(event.get_id()) is not None:
            del event
            raise RepoError("id deja existent")
        self.__events.append(event)

    def modify_date(self, event: Event, new_date: datetime):
        self.find(event)
        event.set_date(new_date)

    def modify_duration(self, event: Event, new_duration: int):
        self.find(event)
        event.set_duration(new_duration)

    def modify_description(self, event: Event, new_desc):
        self.find(event)
        event.set_description(new_desc)

    def delete(self, event):
        self.find(event)
        self.__events.remove(event)
        del event

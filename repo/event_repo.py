import datetime

from domain.event import Event
from repo.repo_error import RepoError


class EventRepo(object):
    """
        repository class that retains a list of event objects and performs CRUD operation on it
        it only works with existent objects.
        it is able to delete invalid objects
        """

    def __init__(self, events: list):
        self.__events = events

    # returns all events from self. repo
    def get_all(self):
        return self.__events

    def find(self, event):
        """
        checks if an events exist or not in self repository
        :param event: event object
        :return: -
        :raises: RepoError if the event doesn't exist.
        :obs: it deletes the event object if it doesn't exist
        """
        if event not in self.__events:
            del event
            raise RepoError("evenimentul nu exista")

    def find_by_id(self, e_id):
        """
        checks if an event-id exist or not in self repo
        :param e_id: id to be found
        :return: an event object with given id or None if doesn't exist
        """
        for event in self.__events:
            if event.get_id() == e_id:
                return event
        return None

    def add(self, event):
        """
        adds an event in repo
        :param event: event to be added
        :raises: RepoError if given event has an id that already exist in repo
        """
        if self.find_by_id(event.get_id()) is not None:
            del event
            raise RepoError("id deja existent")
        self.__events.append(event)

    def modify_date(self, event: Event, new_date: datetime):
        """
        modifies date for an event
        :param event: event to be modified
        :param new_date: new date to be changed
        :raises: RepoError if event doesn't exist
        """
        self.find(event)
        event.set_date(new_date)

    def modify_duration(self, event: Event, new_duration: int):
        """
        modifies duration for an event
        :param event: event to be modified
        :param new_duration: new duration to be changed
        :raises: RepoError if event doesn't exist
        """
        self.find(event)
        event.set_duration(new_duration)

    def modify_description(self, event: Event, new_desc):
        """
        modifies description for an event
        :param event: event to be modified
        :param new_desc: new description to be changed
        :raises: RepoError if event doesn't exist
        """
        self.find(event)
        event.set_description(new_desc)

    def delete(self, event):
        """
        deletes an event from repo
        :param event: event to be deleted
        :raises: RepoError if event doesn't exist
        """
        self.find(event)
        self.__events.remove(event)
        del event

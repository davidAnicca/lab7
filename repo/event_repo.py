import datetime

from domain.event import Event
from repo.repo_error import RepoError
from repo.sale_repo import SaleRepo


class EventRepo(object):
    """
        repository class that retains a list of event objects and performs CRUD operation on it
        it only works with existent objects.
        it is able to delete invalid objects
        """

    def __init__(self, events: list):
        self._events = events

    # returns all events from self. repo
    def get_all(self):
        return self._events

    def find(self, event: Event):
        """
        looks for an event in repo with the same id
        :param event: event to be found
        :return: found event
        :raises: repo error if the event cannot be found
        """
        for e in self._events:
            if e == event:
                return e
        raise RepoError("evenimentul nu exista")

    def add(self, event):
        """
        adds an event in repo
        :param event: event to be added
        :raises: RepoError if given event has an id that already exist in repo
        """
        try:
            self.find(event)
        except RepoError:
            self._events.append(event)
            return
        raise RepoError("id deja existent")

    def modify(self, event):
        """
        changes an event instance with another
        :param event: new event
        :raises: RepoError if the event cannot be found
        """
        old_event = self.find(event)
        self._events.remove(old_event)
        self._events.append(event)
        old_event = event

    def delete(self, event):
        """
        deletes an event from repo and all sales with that event
        :param sale_repo: sale repo
        :param event: event to be deleted
        :raises: RepoError if event doesn't exist
        """
        self.find(event)
        self._events.remove(event)
        del event

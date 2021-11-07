from repo.repo_error import RepoError


class EventRepo(object):

    def __init__(self, events):
        self.__events = events

    def get_all(self):
        return self.__events

    def find(self, event):
        if event not in self.__events:
            del event
            raise RepoError("evenimentul nu exista")


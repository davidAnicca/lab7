from repo.person_repo import PersonRepo


class PersonLogic(object):
    def __init__(self, person_repo: PersonRepo):
        self.__person_repo = person_repo

from unittest import TestCase

from repo.person_repo_dto import PersonRepoDTO


class DtoTest(TestCase):
    def __init__(self):
        self.__person_repo = PersonRepoDTO([])


import random
from unittest import TestCase

from controller.person_srv import PersonService
from controller.random_generator import RandomGen
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


class RandomGenT(TestCase):
    def __init__(self):
        self.__person_repo = PersonRepo([])
        self.__person_srv = PersonService(self.__person_repo, SaleRepo([]))

    def test_generate_persons(self):
        randomGenerator = RandomGen(self.__person_srv)
        number = random.randint(5, 20)
        randomGenerator.generate_persons(number)
        persons = self.__person_repo.get_all()
        print(str(number) + " persoane: ")
        if len(persons) != number:
            self.fail()
        print("\nnume:" + (" " * (25 - len("nume:"))) + \
        "adresă:" + (" " * (30 - len("adresă:"))) + "  id: ")
        for person in persons:
            print(str(person))
        print()



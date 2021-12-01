import random
from unittest import TestCase

from controller.person_srv import PersonService
from controller.random_generator import RandomGen
from repo.person_repo import PersonRepo
from repo.sale_repo import SaleRepo


class RandomGenT(TestCase):

    def setUp(self) -> None:
        self.person_repo = PersonRepo([])
        self.person_srv = PersonService(self.person_repo, SaleRepo([]))

    def tearDown(self) -> None:
        del self.person_repo
        del self.person_srv

    def test_generate_persons(self):
        random_generator = RandomGen(self.person_srv)
        number = random.randint(5, 20)
        random_generator.generate_persons(number)
        persons = self.person_repo.get_all()
        print(str(number) + " persoane: ")
        self.assertEqual(len(persons), number)
        print("\nnume:" + (" " * (25 - len("nume:"))) + \
        "adresă:" + (" " * (30 - len("adresă:"))) + "  id: ")
        for person in persons:
            print(str(person))
        print()



import random

from controller.person_srv import PersonService
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError


class RandomGen(object):
    def __init__(self, person_srv: PersonService):
        self.__person_srv = person_srv

    def generate_person_info(self):
        p_id = random.randint(0, 100)
        first_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVQXYZ")
        random_letters = [random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(1, random.randint(5, 20))]
        p_name = first_letter
        for random_letter in random_letters:
            p_name += random_letter
        random_letters = [random.choice("abc1234567890d  efg hijk lmnop qrstuvw xyz ") for _ in range(1, random.randint(5, 30))]
        p_address = ""

        for random_letter in random_letters:
            p_address += random_letter
        return int(p_id), p_name.strip(), p_address.strip()

    def generate_persons(self, number_of_persons: int):
        index = 1
        while index <= number_of_persons:
            person_info = self.generate_person_info()
            try:
                self.__person_srv.add_person(person_info[0], person_info[1], person_info[2])
                index += 1
            except RepoError:
                pass



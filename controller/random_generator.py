import datetime
import random

from controller.event_srv import EventService
from controller.person_srv import PersonService
from repo.person_repo import PersonRepo
from repo.repo_error import RepoError


class RandomGen(object):
    def __init__(self, service):
        self.__service = service

    def generate_sale_info(self):
        p_id = random.randint(0, 20)
        e_id = random.randint(0, 20)
        return p_id, e_id

    def generate_sales(self, number):
        if number > 40:
            raise Exception("număr prea mare de generări")
        index = 1
        while index <= number:
            params = self.generate_sale_info()
            try:
                self.__service.add_sale(params[0], params[1])
                index += 1
            except RepoError:
                pass


    def generate_event_info(self):
        e_id = random.randint(0, 20)
        letters = [random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(1, random.randint(5, 20))]
        e_des = ""
        for letter in letters:
            e_des += letter
        today = datetime.date.today()
        date = today + datetime.timedelta(days=random.randint(1, 100))
        duration = random.randint(1, 24)
        return e_id, date, duration, e_des

    def generate_events(self, number):
        if number > 10:
            raise Exception("număr prea mare de generări")
        index = 1
        while index <= number:
            info = self.generate_event_info()
            try:
                self.__service.add_event(info[0], info[1], info[2], info[3])
                index += 1
            except RepoError:
                pass

    def generate_person_info(self):
        p_id = random.randint(0, 20)
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
        if number_of_persons > 10:
            raise Exception("număr prea mare de generări")
        index = 1
        while index <= number_of_persons:
            person_info = self.generate_person_info()
            try:
                self.__service.add_person(person_info[0], person_info[1], person_info[2])
                index += 1
            except RepoError:
                pass



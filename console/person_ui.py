from controller.person_srv import PersonService
from controller.random_generator import RandomGen


class PersonUi(object):

    def __init__(self, person_srv: PersonService):
        self.__person_srv = person_srv

    def show_all(self, command):
        persons = self.__person_srv.get_all()
        for person in persons:
            print(person)

    def random(self, command):
        rand = RandomGen(self.__person_srv)
        number = int(command.split()[1])
        rand.generate_persons(number)

from console.command_error import CommandError
from console.strings import strings
from controller.person_srv import PersonService
from controller.random_generator import RandomGen


class PersonUi(object):

    def __init__(self, person_srv: PersonService):
        self.__person_srv = person_srv

    # p
    def show_all(self, command):
        persons = self.__person_srv.get_all()
        for person in persons:
            print(person)

    # rp [number]
    def random(self, command):
        if len(command.split()) >2:
            raise CommandError(strings["rp"])
        rand = RandomGen(self.__person_srv)
        number = 1
        if len(command.split()) == 2:
            number = int(command.split()[1])
        rand.generate_persons(number)

    # addp [id] [name] [address]
    def add(self, command):
        params = command.split()
        if len(params) != 4:
            raise CommandError(strings["addp"])
        self.__person_srv.add_person(int(params[1]), params[2], params[3])

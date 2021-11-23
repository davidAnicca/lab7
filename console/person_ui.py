from console.command_error import CommandError
from console.strings import strings
from controller.person_srv import PersonService
from controller.random_generator import RandomGen


class PersonUi(object):

    def __init__(self, person_srv: PersonService):
        self.__person_srv = person_srv

    def printer(self, collection):
        for element in collection:
            print(str(element))

    # p
    def show_all(self, command):
        persons = self.__person_srv.get_all()
        self.printer(persons)

    # rp [number]
    def random(self, command):
        if len(command.split()) > 2:
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

    # pmn [id] [name]
    def mod_n(self, command):
        params = command.split()
        if len(params) < 3:
            raise CommandError(strings["pmn"])
        name = ""
        for word in params[2:]:
            name += word + " "
        self.__person_srv.modify_name(int(params[1]), name)

    # pma [id] [adresa]
    def mod_a(self, command):
        params = command.split()
        if len(params) < 3:
            raise CommandError(strings["pma"])
        address = ""
        for word in params[2:]:
            address += word + " "
        self.__person_srv.modify_address(int(params[1]), address)

    # pdel [id]
    def delete(self, command):
        params = command.split()
        if len(params) != 2:
            raise CommandError(strings["pdel"])
        self.__person_srv.delete_person(int(params[1]))

    # a
    def active(self, command):
        self.printer(self.__person_srv.get_active())

    # eo [id]
    def events_ordered_date(self, command):
        params = command.split()
        if len(params) != 2:
            raise CommandError(strings["eo"])
        self.printer(self.__person_srv.events_date(int(params[1])))

    # eod [id]
    def events_ordered_dur(self, command):
        params = command.split()
        if len(params) != 2:
            raise CommandError(strings["eod"])

        self.printer(self.__person_srv.events_desc(int(params[1])))

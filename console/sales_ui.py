from console.command_error import CommandError
from controller.random_generator import RandomGen
from controller.sale_srv import SaleService
from console.strings import strings


class SalesUi(object):
    def __init__(self, sale_srv: SaleService):
        self.__sale_srv = sale_srv

    # s
    def show(self, command):
        sales = self.__sale_srv.get_all()
        for sale in sales:
            print(str(sale))

    # ins
    def add(self, command):
        info = command.split()
        if len(info) != 3:
            raise CommandError(strings["ins"])
        self.__sale_srv.add_sale(int(info[1]), int(info[2]))

    # rs
    def random(self, command):
        if len(command.split()) > 2:
            raise CommandError(strings["rs"])
        number = 1
        if len(command.split()) == 2:
            number = int(command.split()[1])
        rand = RandomGen(self.__sale_srv)
        if number >= self.__sale_srv.possible_size():
            raise Exception("nu există suficiente persoane și evenimente pentru a genera")

        rand.generate_sales(number)

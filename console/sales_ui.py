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
            print(strings["ins"])
        self.__sale_srv.add_sale(int(info[1]), int(info[2]))

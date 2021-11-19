class Person(object):

    def __init__(self, p_id, p_name, p_address):
        self.__p_id = p_id
        self.__p_name = p_name
        self.__p_address = p_address

    def get_id(self):
        return self.__p_id

    def get_name(self):
        return self.__p_name

    def get_address(self):
        return self.__p_address

    def set_name(self, p_name):
        self.__p_name = p_name

    def set_address(self, p_address):
        self.__p_address = p_address

    def __str__(self):
        return self.__p_name + (" "*(25-len(self.__p_name))) +\
               self.__p_address + (" "*(30-len(self.__p_address))) + "  id: " + str(self.__p_id)






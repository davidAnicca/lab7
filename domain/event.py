import datetime


class Event(object):

    def __init__(self, e_id: int, e_date: datetime, e_duration: int, e_des: str):
        self.__e_id = e_id
        self.__e_date = e_date
        self.__e_duration = e_duration
        self.__e_des = e_des

    def get_id(self):
        return self.__e_id

    def get_date(self):
        return self.__e_date

    def get_duration(self):
        return self.__e_duration

    def get_description(self):
        return self.__e_des

    def set_date(self, e_date):
        self.__e_date = e_date

    def set_duration(self, e_duration):
        self.__e_duration = e_duration

    def set_description(self, e_description):
        self.__e_des = e_description

    def __str__(self):
        return str(self.__e_id)


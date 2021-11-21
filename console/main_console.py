from console.event_ui import EventUi
from console.person_ui import PersonUi
from controller.event_srv import EventService
from controller.person_srv import PersonService
from controller.sale_srv import SaleService
from repo.repo_error import RepoError
from validation.validation_error import ValidationError


class MainConsole(object):
    def __init__(self, person_srv: PersonService, event_srv: EventService, sale_srv: SaleService):
        self.__person_srv = person_srv
        self.__event_srv = event_srv
        self.__sale_srv = sale_srv
        self.__p_ui = PersonUi(person_srv)
        self.__e_ui = EventUi(event_srv)
        self.__commands = {
            "p": self.__p_ui.show_all,
            "rp": self.__p_ui.random,
            "e": self.__e_ui.show_all,
            "re": self.__e_ui.random,
            "addp": self.__p_ui.add,
            "adde": self.__e_ui.add,
        }

    def run_console(self):
        while True:
            command = input("@>")
            command = command.strip()
            if command == "":
                continue
            if command == "exit":
                return
            try:
                method = self.__commands[command.split()[0]](command)
            except KeyError:
                print("comandă invalidă")
            except ValidationError as e:
                print(str(e))
            except ValueError:
                print("imposibil de transformat în număr")
            except TypeError:
                print("imposibil de transformat")
            except Exception as e:
                print(str(e))

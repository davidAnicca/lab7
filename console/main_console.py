from console import strings
from console.event_ui import EventUi
from console.person_ui import PersonUi
from console.sales_ui import SalesUi
from controller.event_srv import EventService
from controller.person_srv import PersonService
from controller.sale_srv import SaleService
from repo.repo_error import RepoError
from validation.validation_error import ValidationError
import Levenshtein as StringComparison


class MainConsole(object):
    def __init__(self, person_srv: PersonService, event_srv: EventService, sale_srv: SaleService):
        self.__person_srv = person_srv
        self.__event_srv = event_srv
        self.__sale_srv = sale_srv
        self.__p_ui = PersonUi(person_srv)
        self.__e_ui = EventUi(event_srv)
        self.__s_ui = SalesUi(sale_srv)
        self.__commands = {
            "p": self.__p_ui.show_all,
            "rp": self.__p_ui.random,
            "e": self.__e_ui.show_all,
            "re": self.__e_ui.random,
            "addp": self.__p_ui.add,
            "adde": self.__e_ui.add,
            "s": self.__s_ui.show,
            "ins": self.__s_ui.add,
            "h": self.help,
        }

    # h
    def help(self, command):
        for com in strings.strings.values():
            print(str(com), end="  ;  ")
        print()

    def run_console(self):
        # print(StringComparison.ratio("addc", "addp"))
        while True:
            command = input("\n@>")
            command = command.strip()
            if command == "":
                continue
            if command == "exit":
                return
            try:
                method = self.__commands[command.split()[0]](command)
            except KeyError:
                print("comandă invalidă")
                cmd = command.split()
                commands = strings.strings.keys()
                print("ai putea încerca: ")
                for com in commands:
                    r = StringComparison.ratio(cmd[0], str(com))
                    if r > 0.5:
                        print(strings.strings[str(com)])
            except ValidationError as e:
                print(str(e))
            except ValueError:
                print("imposibil de transformat în număr")
            except TypeError:
                print("imposibil de transformat")
            except Exception as e:
                print(str(e))

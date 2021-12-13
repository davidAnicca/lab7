from console.main_console import MainConsole
from controller.event_srv import EventService
from controller.person_srv import PersonService
from controller.sale_srv import SaleService
from repo.dto.event_repo_dto import EventRepoDTO
from repo.dto.sale_repo_dto import SaleRepoDTO
from repo.event_repo import EventRepo
from repo.dto.person_repo_dto import PersonRepoDTO
from repo.sale_repo import SaleRepo
from tester.tests import Tests


class Main(object):

    def run(self):
        Tests().run_tests()

        person_repo = PersonRepoDTO([], "repo/files/persons.csv")
        event_repo = EventRepoDTO([], "repo/files/events.csv")
        sale_repo = SaleRepoDTO([], person_repo, event_repo, "repo/files/sales.csv")

        person_srv = PersonService(person_repo, sale_repo)
        event_srv = EventService(event_repo, sale_repo)
        sale_srv = SaleService(person_repo, event_repo, sale_repo)
        main_console = MainConsole(person_srv, event_srv, sale_srv)
        main_console.run_console()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main = Main()
    main.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

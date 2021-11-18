from tester.controller_tests import ControllerTest
from tester.logic_tests import LogicTests
from tester.test_event_repo import TestEventRepo
from tester.test_person_repo import TestPersonRepo
from tester.test_sale_repo import TestSaleRepo
from tester.validation_tests import ValidationTests


class Tests(object):

    @staticmethod
    def run_tests():
        #person repo tests:
        test_person_repo = TestPersonRepo()
        test_person_repo.test_find()
        test_person_repo.test_find_by_id()
        test_person_repo.test_add()
        test_person_repo.test_modify_name()
        test_person_repo.test_modify_address()
        test_person_repo.test_delete()
        del test_person_repo

        #event repo tests:
        test_event_repo = TestEventRepo()
        test_event_repo.test_find()
        test_event_repo.test_find_by_id()
        test_event_repo.test_add()
        test_event_repo.test_modify_date()
        test_event_repo.test_modify_duration()
        test_event_repo.test_modify_description()
        test_event_repo.test_delete()
        del test_event_repo

        #sales repo tests:
        test_sales_repo = TestSaleRepo()
        test_sales_repo.test_find()
        test_sales_repo.test_find_by_pair()
        test_sales_repo.test_add()
        del test_sales_repo

        #logic tests:
        logic_tests = LogicTests()
        logic_tests.test_get_event_w_max_duration()
        logic_tests.test_get_20_p()
        logic_tests.test_get_person_with_most_events()
        logic_tests.test_give_all_events_ordered_by_date()
        logic_tests.test_give_all_events_ordered_by_description()
        del logic_tests

        #validation test:
        validation_tests = ValidationTests()
        validation_tests.test_validate_event()
        del validation_tests

        #controller test:
        controler_tests = ControllerTest()
        controler_tests.test_create_person()
        controler_tests.test_add_person()
        controler_tests.test_delete()
        controler_tests.test_create_event()
        controler_tests.test_add_event()
        controler_tests.test_delete_event()
        controler_tests.test_modify_event()

        print("teste trecute cu succes")
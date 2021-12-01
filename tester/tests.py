import unittest

from controller.random_generator import RandomGen
from tester import controller_tests
from tester.controller_tests import ControllerTest

from tester.logic_tests import LogicTests
from tester.random_gen_t import RandomGenT
from tester.test_event_repo import TestEventRepo
from tester.test_person_repo import TestPersonRepo
from tester.test_sale_repo import TestSaleRepo
from tester.validation_tests import ValidationTests


class Tests(object):

    @staticmethod
    def run_tests():
        # person repo tests:   #todo
        test_person_repo = TestPersonRepo()
        test_person_repo.test_find()
        test_person_repo.test_find_by_id()
        test_person_repo.test_add()
        test_person_repo.test_modify()
        test_person_repo.test_delete()
        del test_person_repo

        # event repo tests:   #todo
        test_event_repo = TestEventRepo()
        test_event_repo.test_find()
        test_event_repo.test_add()
        test_event_repo.test_modify()
        test_event_repo.test_delete()
        del test_event_repo

        # sales repo tests:    #todo
        test_sales_repo = TestSaleRepo()
        test_sales_repo.test_find()
        test_sales_repo.test_find_by_pair()
        test_sales_repo.test_add()
        del test_sales_repo

        # logic tests:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(LogicTests)
        unittest.TextTestRunner().run(suite)

        # validation test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ValidationTests)
        unittest.TextTestRunner().run(suite)

        # controller test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ControllerTest)
        unittest.TextTestRunner().run(suite)

        # generator test:
        # suite = unittest.defaultTestLoader.loadTestsFromTestCase(RandomGenT)
        # unittest.TextTestRunner().run(suite)

    # print("teste trecute cu succes")

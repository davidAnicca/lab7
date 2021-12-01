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

        test_classes = [TestPersonRepo,
                        TestEventRepo,
                        TestSaleRepo,
                        LogicTests,
                        ValidationTests,
                        ControllerTest]

        for test_class in test_classes:
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_class)
            unittest.TextTestRunner().run(suite)

        # generator test:
        # suite = unittest.defaultTestLoader.loadTestsFromTestCase(RandomGenT)
        # unittest.TextTestRunner().run(suite)

    # print("teste trecute cu succes")

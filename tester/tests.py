from tester.test_event_repo import TestEventRepo
from tester.test_person_repo import TestPersonRepo

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

        #event repo tests:
        test_event_repo = TestEventRepo()
        test_event_repo.test_find()
import tasks


class TestTasksNumOfSublists:

        def test_num_of_sublists_positive_1(self):
            assert tasks.num_of_sublists([[1, 2, 3]]) == 1

        def test_num_of_sublists_positive_1(self):
            assert tasks.num_of_sublists([[1, 2, 3], [1, 6, 8], [1, 9]]) == 3

        def test_num_of_sublists_empty(self):
            assert tasks.num_of_sublists([]) == 0

        def test_num_of_sublists_zero(self):
            assert tasks.num_of_sublists([1, 4, 7]) == 0

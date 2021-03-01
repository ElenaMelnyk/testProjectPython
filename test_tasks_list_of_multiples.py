import pytest

import tasks


class TestTasksListOfMultiples:
    def test_list_of_multiples(self):
        assert tasks.list_of_multiples (7, 5) == [7, 14, 21, 28, 35]

    @pytest.mark.parametrize('test_input_1, test_input_2, expect',
                             [
                                 (12, 10, [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
                             ])
    def test_list_of_multiples(self, test_input_1, test_input_2, expect):
        assert tasks.list_of_multiples (test_input_1, test_input_2) == expect
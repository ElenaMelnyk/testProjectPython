import pytest

import tasks


class TestTasksEmptyingValues:

    @pytest.mark.parametrize("test_int, expect", [([3, 2, 0], [0, 0, 0])])
    def test_emptying_values_int(self, test_int, expect):
        assert tasks.emptying_values(test_int) == expect

    @pytest.mark.parametrize("test_mix, expect", [([7, 3.14, 'cat'], [0, 0.0, ''])])
    def test_emptying_values_mix(self, test_mix, expect):
        assert tasks.emptying_values(test_mix) == expect

    @pytest.mark.parametrize("test_mix_2, expect", [([[1, 2, 3], (1,2,3), {1,2,3}], [[], (), set()])])
    def test_emptying_values_mix_2(self, test_mix_2, expect):
        assert tasks.emptying_values(test_mix_2) == expect

    @pytest.mark.parametrize("test_None, expect", [([None], [None])])
    def test_emptying_values_None(self, test_None, expect):
        assert tasks.emptying_values(test_None) == expect
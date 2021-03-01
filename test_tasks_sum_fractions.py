import pytest

import tasks


class TestTasksSumFractions:

    @pytest.mark.parametrize("test_lst, expect", [([[18, 13], [4, 5]], 2)])
    def test_sum_fractions_1(self, test_lst, expect):
        assert tasks.sum_fractions (test_lst) == expect

    @pytest.mark.parametrize("test_lst, expect", [([[36, 4], [22, 60]], 9)])
    def test_sum_fractions_2(self, test_lst, expect):
        assert tasks.sum_fractions(test_lst) == expect

    @pytest.mark.parametrize("test_lst, expect", [([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]], 11)])
    def test_sum_fractions_3(self, test_lst, expect):
        assert tasks.sum_fractions(test_lst) == expect

    @pytest.mark.parametrize("test_lst, expect", [([[36, 4], [22, 60]], "9")])
    def test_sum_fractions_negative(self, test_lst, expect):
        assert tasks.sum_fractions(test_lst) != expect
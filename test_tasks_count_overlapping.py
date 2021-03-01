import pytest

import tasks


class TestTasksCountOverlapping:

    @pytest.mark.parametrize("test_lst, test_number, expect", [([[1, 2], [2, 3], [3, 4]], 5, 0)])
    def test_count_overlapping_zero(self, test_lst, test_number, expect):
        assert tasks.count_overlapping(test_lst, test_number) == expect

    @pytest.mark.parametrize("test_lst, test_number, expect", [([[1, 2], [5, 6], [5, 7]], 5, 2)])
    def test_count_overlapping_into(self, test_lst, test_number, expect):
        assert tasks.count_overlapping(test_lst, test_number) == expect

    @pytest.mark.parametrize("test_lst, test_number, expect", [([[1, 2], [2, 3], [3, 4]], 4, 2)])
    def test_count_overlapping_zero_negative(self, test_lst, test_number, expect):
        assert tasks.count_overlapping(test_lst, test_number) != expect
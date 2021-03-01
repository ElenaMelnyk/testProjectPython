import pytest

import tasks


class TestTasksGetIndices:

    @pytest.mark.parametrize("test_lst, test_item, expect", [(["a", "a", "b", "a", "b", "a"], "a", [0, 1, 3, 5])])
    def test_get_indices_list(self, test_lst, test_item, expect):
        assert tasks.get_indices(test_lst, test_item) == expect

    @pytest.mark.parametrize("test_lst, test_item, expect", [([1, 5, 5, 2, 7], 7, [4])])
    def test_get_indices_number(self, test_lst, test_item, expect):
        assert tasks.get_indices(test_lst, test_item) == expect

    @pytest.mark.parametrize("test_lst, test_item, expect", [([1, 5, 5, 2, 7], 8, [])])
    def test_get_indices_empty(self, test_lst, test_item, expect):
        assert tasks.get_indices(test_lst, test_item) == expect

    @pytest.mark.parametrize("test_lst, test_item, expect", [([1, 8], 8, [0])])
    def test_get_indices_negative_1(self, test_lst, test_item, expect):
        assert tasks.get_indices(test_lst, test_item) != expect

    @pytest.mark.parametrize("test_lst, test_item, expect", [({1, "8"}, "8", [1])])
    def test_get_indices_pos(self, test_lst, test_item, expect):
        assert tasks.get_indices(test_lst, test_item) == expect
import pytest

import tasks


class TestTasksConcat:

    @pytest.mark.parametrize("test_lists, expect", [(([1, 2, 3], [4, 5], [6, 7]), [1, 2, 3, 4, 5, 6, 7])])
    def test_concat_1(self, test_lists, expect):
        assert tasks.concat(test_lists) == expect

    @pytest.mark.parametrize("test_lists, expect", [([[1], [2], [3], [4], [5], [6], [7]], [1, 2, 3, 4, 5, 6, 7])])
    def test_concat_2(self, test_lists, expect):
        assert tasks.concat(test_lists) == expect

    @pytest.mark.parametrize("test_lists, expect", [([4, 4, 4, 4, 4], [4, 4, 4, 4, 4])])
    def test_concat_3(self, test_lists, expect):
        assert tasks.concat(test_lists) == expect
import pytest

import tasks


class TestTasksSquareAreasDifference:

    @pytest.mark.parametrize('test_input,expect', [(5, 50)])
    def test_square_areas_difference(self, test_input, expect):
        assert tasks.square_areas_difference(test_input) == expect

    def test_square_areas_difference_null(self):
        assert tasks.square_areas_difference(0) == 0

    def test_square_areas_difference_null(self):
        assert tasks.square_areas_difference(-10) == None


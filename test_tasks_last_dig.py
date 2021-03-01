import pytest

import tasks


class TestTasksLastzDig:

    @pytest.mark.parametrize("input_a, input_b, input_c", [(25, 21, 125)])
    def test_last_dig_True_1(self, input_a, input_b, input_c):
        assert tasks.last_dig(input_a, input_b, input_c) is True

    @pytest.mark.parametrize("input_a, input_b, input_c", [(55, 226, 5190)])
    def test_last_dig_True_2(self, input_a, input_b, input_c):
        assert tasks.last_dig(input_a, input_b, input_c) is True

    @pytest.mark.parametrize("input_a, input_b, input_c", [(25, 21, 120)])
    def test_last_dig_False(self, input_a, input_b, input_c):
        assert tasks.last_dig(input_a, input_b, input_c) is False

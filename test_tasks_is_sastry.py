import pytest

import tasks


class TestTasksIsSastry:

    @pytest.mark.parametrize("test_number", [183])
    def test_is_sastry_True(self, test_number):
        assert tasks.is_sastry(test_number) is True

    @pytest.mark.parametrize("test_number", [184])
    def test_is_sastry_False(self, test_number):
        assert tasks.is_sastry(test_number) is False

    @pytest.mark.parametrize("test_number", [0])
    def test_is_sastry_True_zero(self, test_number):
        assert tasks.is_sastry(test_number) is True

    @pytest.mark.parametrize("test_number", [00])
    def test_is_sastry_None(self, test_number):
        assert tasks.is_sastry(test_number) is None
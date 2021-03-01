import pytest

import tasks


class TestTasksIsRepdigit:

    @pytest.mark.parametrize("test_number", [555, 44, 999])
    def test_is_repdigit_positve_1(self, test_number):
        assert tasks.is_repdigit(test_number) is True

    @pytest.mark.parametrize("test_number", [0])
    def test_is_repdigit_positve_2(self, test_number):
        assert tasks.is_repdigit(test_number) is True

    @pytest.mark.parametrize("test_number", [-22])
    def test_is_repdigit_negative(self, test_number):
        assert tasks.is_repdigit(test_number) is False
import pytest

import tasks


class TestTasksStupidAddition:

    @pytest.mark.parametrize ("test_par1, test_par2, expect", [(1, 2, "12")])
    def test_stupid_addition_str(self, test_par1, test_par2, expect):
        assert tasks.stupid_addition (test_par1, test_par2) == expect

    @pytest.mark.parametrize("test_par1, test_par2, expect", [("3", "4", 7)])
    def test_stupid_addition_int(self, test_par1, test_par2, expect):
        assert tasks.stupid_addition(test_par1, test_par2) == expect

    @pytest.mark.parametrize("test_par1, test_par2, expect", [("3", "-4", -1)])
    def test_stupid_addition_int2(self, test_par1, test_par2, expect):
        assert tasks.stupid_addition(test_par1, test_par2) == expect

    @pytest.mark.parametrize("test_par1, test_par2, expect", [("3", 4, None)])
    def test_stupid_addition_None(self, test_par1, test_par2, expect):
        assert tasks.stupid_addition(test_par1, test_par2) == expect
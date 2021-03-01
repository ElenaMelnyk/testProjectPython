import pytest

import tasks


class TestTasksVolShell:
    @pytest.mark.parametrize ('test_r1, test_r2, expect', [(3, 3, 0)])
    def test_vol_shell_zero(self, test_r1, test_r2, expect):
        assert tasks.vol_shell (test_r1, test_r2) == expect

    @pytest.mark.parametrize('test_r1, test_r2, expect', [(7, 2, 1403.245)])
    def test_vol_shell_positive(self, test_r1, test_r2, expect):
        assert tasks.vol_shell(test_r1, test_r2) == expect

    @pytest.mark.parametrize_invers_R('test_r1, test_r2, expect', [(2, 7, 1403.245)])
    def test_vol_shell(self, test_r1, test_r2, expect):
        assert tasks.vol_shell(test_r1, test_r2) == expect

    @pytest.mark.parametrize_negative('test_r1, test_r2, expect', [(-10, -50, None)])
    def test_vol_shell(self, test_r1, test_r2, expect):
        assert tasks.vol_shell(test_r1, test_r2) == expect
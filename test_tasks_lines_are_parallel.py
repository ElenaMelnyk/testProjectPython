import pytest

import tasks


class TestTasksLinesAreParallel:

    @pytest.mark.parametrize ("input_line1_params, input_line2_params, expect",
                              [
                                  ([1, 2, 3], [1, 2, 4], True)
                              ])
    def test_lines_are_parallel_true_1(self, input_line1_params, input_line2_params, expect):
        assert tasks.lines_are_parallel(input_line1_params, input_line2_params) == expect


    @pytest.mark.parametrize("input_line1_params, input_line2_params, expect",
                             [
                                 ([0, 1, 5], [0, 1, 5], True)
                             ])
    def test_lines_are_parallel_true_2(self, input_line1_params, input_line2_params, expect):
        assert tasks.lines_are_parallel(input_line1_params, input_line2_params) == expect


    @pytest.mark.parametrize("input_line1_params, input_line2_params, expect",
                             [
                                 ([0, 0, 0], [0, 0, 0], None)
                             ])
    def test_lines_are_parallel_none(self, input_line1_params, input_line2_params, expect):
        assert tasks.lines_are_parallel(input_line1_params, input_line2_params) == expect


    @pytest.mark.parametrize("input_line1_params, input_line2_params, expect",
                             [
                                 ([2, 4, 1], [4, 2, 1], False)
                             ])
    def test_lines_are_parallel_false(self, input_line1_params, input_line2_params, expect):
        assert tasks.lines_are_parallel(input_line1_params, input_line2_params) == expect

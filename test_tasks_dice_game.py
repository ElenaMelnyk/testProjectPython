import pytest

import tasks


class TestTasksDiceGame:

    @pytest.mark.parametrize("test_input, expect", [(([(1, 2), (3, 4), (5, 6)]), 21)])
    def test_dice_game_positive(self, test_input, expect):
        assert tasks.dice_game(test_input) ==expect

    @pytest.mark.parametrize("test_input, expect", [(([(1, 1), (3, 4), (5, 6)]), 0)])
    def test_dice_game_zero(self, test_input, expect):
        assert tasks.dice_game(test_input) == expect

    @pytest.mark.parametrize("test_input, expect", [([], 0)])
    def test_dice_game_empty(self, test_input, expect):
        assert tasks.dice_game(test_input) == expect

    @pytest.mark.parametrize("test_input, expect", [(([(1, 2), (3, 4)]), None)])
    def test_dice_game_None_1(self, test_input, expect):
        assert tasks.dice_game(test_input) == expect

    @pytest.mark.parametrize("test_input, expect", [(([(1, 2), (3), (2, 4)]), None)])
    def test_dice_game_None_2(self, test_input, expect):
        assert tasks.dice_game(test_input) == expect

    @pytest.mark.parametrize("test_input, expect", [(([(1, 2), (3, -4), (2, -4)]), None)])
    def test_dice_game_None_2(self, test_input, expect):
        assert tasks.dice_game(test_input) == expect

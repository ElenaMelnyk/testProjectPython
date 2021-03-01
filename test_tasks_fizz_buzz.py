import pytest

import tasks


class TestTasksFizzBuzz:
    def test_fizz_buzz_div_three(self):
        assert tasks.fizz_buzz(6) == "Fizz"

    def test_fizz_buzz_div_five(self):
        assert tasks.fizz_buzz(25) == "Buzz"

    def test_fizz_buzz_div_three_and_five(self):
        assert tasks.fizz_buzz(15) == "FizzBuzz"

    def test_fizz_buzz_div_self(self):
        assert tasks.fizz_buzz(4) == "4"

    @pytest.mark.parametrize('test_input, expect', [(4, "4")])
    def test_fizz_buzz_div_self(self, test_input, expect):
        assert tasks.fizz_buzz(test_input) == expect
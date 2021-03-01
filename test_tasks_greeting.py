import pytest

import tasks


class TestTasksGreeting:

    @pytest.mark.parametrize ("test_input_name, expect", [("Randy", "Hi! I'm Randy, and I'm from Germany.")])
    def test_greeting_in_list(self, test_input_name, expect):
        assert tasks.greeting(test_input_name) == expect

    @pytest.mark.parametrize("test_input_name, expect", [("Ann", "Hi! I'm a guest.")])
    def test_greeting_not_in_list(self, test_input_name, expect):
        assert tasks.greeting(test_input_name) == expect
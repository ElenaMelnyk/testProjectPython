import tasks


class TestTasksCountUppercase:

    def test_count_uppercase_six(self):
        assert tasks.count_uppercase(['SOLO', 'hello', 'Tea', 'wHat']) == 6

    def test_count_uppercase_zero(self):
        assert tasks.count_uppercase(['hello', 'tea', 'what']) == 0

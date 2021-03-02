import tasks


class TestTasksIsPandigital:
    def test_is_pandigital_true(self):
        assert tasks.is_pandigital(98140723568910) is True

    def test_is_pandigital_true(self):
        assert tasks.is_pandigital(90864523148909) is False

    def test_is_pandigital_false(self):
        assert tasks.is_pandigital(9888144072356891000) is False

    def test_is_pandigital_false_zero(self):
        assert tasks.is_pandigital(0) is False

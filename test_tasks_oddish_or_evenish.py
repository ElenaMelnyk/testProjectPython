import tasks


class TestTasksOddishOrEvenish:

    def test_oddish_or_evenish_Oddish(self):
        assert tasks.oddish_or_evenish(43) == "Oddish"

    def test_oddish_or_evenish_Evenish(self):
        assert tasks.oddish_or_evenish(4433) == "Evenish"

    def test_oddish_or_evenish_Zero(self):
        assert tasks.oddish_or_evenish(0) == None
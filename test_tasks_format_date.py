import tasks


class TestTasksFormatDate:
    def test_format_date(self):
        assert tasks.format_date ("11/12/2002") == "20021211"

    def test_format_date(self):
        assert tasks.format_date ("31/01/2055") == "20550131"

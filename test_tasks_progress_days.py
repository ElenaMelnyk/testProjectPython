import tasks


class TestTasksProgressDays:

        def test_progress_days_positive(self):
            assert tasks.progress_days([3, 4, 1, 2]) == 2

        def test_progress_days_zero_1(self):
            assert tasks.progress_days([3, 3, 3]) == 0

        def test_progress_days_zero_2(self):
            assert tasks.progress_days([3, 2, 1]) == 0

        def test_progress_days_enpty(self):
            assert tasks.progress_days([]) == 0
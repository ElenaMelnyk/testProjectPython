import tasks


class TestTasksSquarePatch:

    def test_square_patch_positive_1(self):
        assert tasks.square_patch(3) == [[3, 3, 3], [3, 3, 3], [3, 3, 3]]

    def test_square_patch_positive_1(self):
        assert tasks.square_patch(1) == [[1]]

    def test_square_patch_zero(self):
        assert tasks.square_patch(0) == []

    def test_square_patch_negative(self):
        assert tasks.square_patch(-1) == []

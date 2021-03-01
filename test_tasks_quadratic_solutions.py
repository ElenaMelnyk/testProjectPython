import tasks


class TestTasksQuadraticSolutions:
    def test_quadratic_solutions_twis(self):
        assert tasks.quadratic_solutions(1, 0, -1) == 2

    def test_quadratic_solutions_twis(self):
        assert tasks.quadratic_solutions(1, 0, 0) == 1

    def test_quadratic_solutions_twis(self):
        assert tasks.quadratic_solutions(1, 0, 1) == 0

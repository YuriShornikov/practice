from main import div_f, sum_f, get_dict

class TestSomething:
    def test_sum(self):
        assert sum_f(4, 2) == 6

    def test_div(self):
        assert div_f(6, 3) == 2
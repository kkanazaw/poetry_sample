from poetry_sample.calc import Calc


def test_sum():
    c = Calc()
    assert 2 == c.sum()

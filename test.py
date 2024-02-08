import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)
    """Позитивный тест на умножение"""
    def test_umnojenie(self):
        assert self.calc.multiply(self, 3, 3) == 9

    """Позитивный тест на деление"""
    def test_delenie(self):
        assert self.calc.division(self, 100, 2) == 50

    """Позитивный тест на вычет"""
    def test_minus(self):
        assert self.calc.subtraction(self, 1000, 999) == 1

    """Позитивный тест на сложение"""
    def test_slojenie(self):
        assert self.calc.adding(self, 4, 4) == 8

    def teardown(self):
        print('Выполнение метода teardown')



import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(5, 3) == 8

    def test_subtraction_success(self):
        assert self.calc.subtraction(10, 4) == 6

    def test_multiplication_success(self):
        assert self.calc.multiplication(7, 2) == 14

    def test_division_success(self):
        assert self.calc.division(15, 3) == 5.0


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
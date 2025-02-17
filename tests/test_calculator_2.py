import pytest
from app.calculator import Calculator

# Фикстура для инициализации калькулятора
@pytest.fixture
def calc():
    return Calculator()

class TestCalc:
    def test_adding_success(self, calc):
        assert calc.adding(1, 1) == 4, "Addition test failed"

    def test_adding_unsuccess(self, calc):
        assert calc.adding(1, 1) != 3, "Unsuccessful addition test failed"

    def test_zero_division(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.division(1, 0)

    def test_teardown(self):
        print("Execution method Teardown")
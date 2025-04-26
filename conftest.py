import pytest

from calculator import Calculator
@pytest.fixture
def calculator():
 return Calculator()


class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    # Override other methods similarly...

@pytest.fixture
def precise_calculator():
    return PreciseCalculator(precision=2)

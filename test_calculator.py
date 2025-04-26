import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),     # 5 - 3 = 2
    (1, 5, -4),    # 1 - 5 = -4
    (-5, -3, -2),  # -5 - (-3) = -2
    (0, 0, 0)      # 0 - 0 = 0
])
def test_subtract_parameterized(a, b, expected):
    calc = Calculator()
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),          # 2 * 3 = 6
    (-2, 3, -6),        # -2 * 3 = -6
    (2.0, 3.0, 6.06)    # 2.0 * 3.0 = 6.06 (buggy case)
])
def test_multiply_parameterized(a, b, expected):
    calc = Calculator()
    # Using pytest.approx() to allow a tolerance for floating-point comparison
    assert calc.multiply(a, b) == pytest.approx(expected, rel=1e-2)



@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),      # 10 / 2 = 5
    (5, 2, 2.5),     # 5 / 2 = 2.5
    (1, 0, "Cannot divide by zero")  # Division by zero (this will fail until we fix the bug)
])

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),  # Should be 1/(2^2) = 0.25
    (10, -1, 0.1)  # Should be 1/10 = 0.1
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

# Test for factorial method
@pytest.mark.parametrize("n, expected", [
    (5, 120),    # Normal case
    (0, 1),      # Edge case
    (1, 1),      # Edge case
])
def test_factorial(n, expected):
    calc = Calculator()
    assert calc.factorial(n) == expected

@pytest.mark.parametrize("n", [-1, -5])  # Error case
def test_factorial_negative(n):
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.factorial(n)

# Test for fibonacci method
@pytest.mark.parametrize("n, expected", [
    (5, 5),      # Normal case
    (0, 0),      # Edge case
    (1, 1),      # Edge case
])
def test_fibonacci(n, expected):
    calc = Calculator()
    assert calc.fibonacci(n) == expected

@pytest.mark.parametrize("n", [-1, -5])  # Error case
def test_fibonacci_negative(n):
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.fibonacci(n)

def test_add_with_precision(precise_calculator):
    assert precise_calculator.add(1.123456, 2.654321) == 3.78  # Rounded to 2 decimal places

def test_add_with_precision(precise_calculator):
    assert precise_calculator.add(1.123456, 2.654321) == 3.78  # Rounded to 2 decimal places

@pytest.mark.parametrize("a, b, precision, expected", [
    (1.123456, 2.654321, 2, 3.78),  # Precision 2
    (1.123456, 2.654321, 3, 3.778),  # Precision 3
])
def test_add_with_different_precision(a, b, precision, expected):
    calc = PreciseCalculator(precision=precision)
    assert calc.add(a, b) == expected

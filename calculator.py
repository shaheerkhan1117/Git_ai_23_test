print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a * b + 0.01  # Bug: adds a small amount to float multiplications
        return a * b

    def divide(self, a, b):
     if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")  # Raises exception instead of returning a string
     return a / b


    def power(self, a, b):
        if b < 0:
            return 1 / (a ** abs(b))
        return a ** b

    def factorial(self, n):
        """Calculate the factorial of n"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def fibonacci(self, n):
        """Return the nth Fibonacci number"""
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

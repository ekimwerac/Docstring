class Calculator:
    """A simple calculator class for basic arithmetic operations.

    Usage Examples:
    ----------------
    # Create a Calculator instance
    >>> calc = Calculator()

    # Add two numbers
    >>> calc.add(3, 5)
    8

    # Subtract y from x
    >>> calc.subtract(10, 3)
    7

    # Multiply two numbers
    >>> calc.multiply(4, 6)
    24

    # Divide x by y
    >>> calc.divide(10, 2)
    5.0

    # Handle division by zero
    >>> calc.divide(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """

    def add(self, x, y):
        """Add two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtract y from x."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide x by y. Returns a float."""
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

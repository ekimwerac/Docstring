from calculator import Calculator

def test_calculator_examples():
    """
    >>> calc = Calculator()
    >>> calc.add(3, 5)
    8

    >>> calc.subtract(10, 3)
    7

    >>> calc.multiply(4, 6)
    24

    >>> calc.divide(10, 2)
    5.0

    >>> calc.divide(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """

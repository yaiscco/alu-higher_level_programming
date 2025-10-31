#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result safely.

    Args:
        a: First integer (dividend)
        b: Second integer (divisor)

    Returns:
        The result of the division, or None if division fails
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result

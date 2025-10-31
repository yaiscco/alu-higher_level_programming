#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer safely using {:d} format.

    Args:
        value: Value of any type to attempt printing as integer

    Returns:
        True if value was successfully printed as integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements from a list safely.

    Args:
        my_list: List containing elements of any type
        x: Number of elements to print

    Returns:
        The actual number of elements printed
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count

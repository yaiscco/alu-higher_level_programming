#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers from a list.

    Args:
        my_list: List containing elements of any type
        x: Number of elements to access in the list

    Returns:
        The actual number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count

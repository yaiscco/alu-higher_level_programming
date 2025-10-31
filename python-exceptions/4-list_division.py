#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide elements of two lists element by element.

    Args:
        my_list_1: First list containing any type
        my_list_2: Second list containing any type
        list_length: Length of the result list

    Returns:
        A new list with division results (0 if division fails)
    """
    result = []
    for i in range(list_length):
        div_result = 0
        try:
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            result.append(div_result)
    return result

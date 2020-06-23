import logging


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int):
        logging.error("Invalid input type. Should be integer.")
        return

    if number < 0:
        logging.error("Square root of negative number is undefined.")
        return

    if number == 0 or number == 1:
        return number

    start, end = 1, number
    while start <= end:
        mid = (start + end) // 2
        mid_square = mid * mid

        if mid_square == number:
            return mid
        elif mid_square < number:
            start = mid + 1

        else:
            end = mid - 1
    return start - 1


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (sqrt(None) is None) else "Fail")  # None input
print("Pass" if (sqrt(-10) is None) else "Fail")  # negative input
print("Pass" if (sqrt(4.2) is None) else "Fail")  # None input

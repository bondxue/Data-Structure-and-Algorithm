def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not input_list:
        return -1

    if len(input_list) == 1:
        if input_list[0] == number:
            return 0
        else:
            return -1

    start, end = 0, len(input_list) - 1

    while start + 1 < end:
        mid = (end - start) // 2 + start
        # mid = (start + end) // 2

        if input_list[mid] >= input_list[start]:
            if input_list[start] <= number <= input_list[mid]:
                end = mid
            else:
                start = mid
        else:
            if input_list[mid] <= number <= input_list[mid]:
                start = mid
            else:
                end = mid
        if input_list[start] == number:
            return start
        if input_list[end] == number:
            return end

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])  # test target not in the list
test_function([[], 10])  # test empty input list
test_function([[1], 2])  # test input list with single value
test_function([[1], 0])  # test input list with single value and target is not in the list

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if len(input_list) == 0:
        return 0, 0
    if len(input_list) == 1:
        return input_list[0], 0

    # sort list in descending order
    items = reverse_mergesort(input_list)

    # fill num1 with digits at the odd indices of sorted list
    num1 = 0
    for i in range(0, len(items), 2):
        num1 = num1 * 10 + items[i]

    # fill num2 with digits at the even indices of sorted list
    num2 = 0
    for i in range(1, len(items), 2):
        num2 = num2 * 10 + items[i]

    return num1, num2


def reverse_mergesort(items):
    # sort list in descending order
    if len(items) <= 1:
        return items

    index = len(items) // 2
    left = items[:index]
    right = items[index:]

    left = reverse_mergesort(left)
    right = reverse_mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Repeating Numbers
test_function([[1, 1, 1, 1, 1], [111, 11]])
test_function([[1, 1, 2, 2, 3, 3, 4, 4], [4321, 4321]])

# Out of order with repeating
test_function([[9, 1, 8, 2, 7, 3, 9], [9831, 972]])

# input list with only single and no element
test_function([[2], [2, 0]])
test_function([[], [0, 0]])

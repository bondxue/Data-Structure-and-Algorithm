def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    i = j = 0  # j records number of '0' and '1'， and i records number of '0'
    for k in range(len(input_list)):
        v = input_list[k]
        input_list[k] = 2
        if v < 2:  # if less than 2, assign 1
            input_list[j] = 1
            j += 1
        if v == 0:  # if equal to 0, assign 0
            input_list[i] = 0
            i += 1

    return input_list

    # bucket = [0] * 3
    # for i in input_list:
    #     bucket[i] += 1
    #
    # del input_list[:]
    # for i in range(3):
    #     for j in range(bucket[i]):
    #         input_list.append(i)
    #
    # return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])  # test empty input list
test_function([1])  # test single value

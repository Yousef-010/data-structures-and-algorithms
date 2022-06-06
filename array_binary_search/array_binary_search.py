from unittest import result


def sort_array(my_list):
    """
    this function sorts an array of integers and return the sorted array in the right case
    and will return empty array in the wrong case
    """
    if len(my_list) == 0:
        return 'Invalid ARRAY SIZE ( EMPTY ARRAY )'
    else:
        for pointer_one in range(len(my_list)):
            for pointer_two in range(pointer_one + 1, len(my_list)):
                if my_list[pointer_one] > my_list[pointer_two]:
                    my_list[pointer_one], my_list[pointer_two] = my_list[pointer_two], my_list[pointer_one]
        return my_list


def array_binary_search(my_list, key):
    """
    this function will take an array and key and try to find the key in the array if
    the key is existing in the array.
    else return -1
    """
    if len(my_list) == 0:
        return 'Invalid ARRAY SIZE ( EMPTY ARRAY )'
    else:
        mid_low_high = 0
        low_index = 0
        high_index = len(my_list) - 1

        while low_index <= high_index:
            mid_low_high = (high_index + low_index) // 2
            if my_list[mid_low_high] < key:
                low_index = mid_low_high + 1
            elif my_list[mid_low_high] > key:
                high_index = mid_low_high - 1
            else:
                return mid_low_high

        return -1

# show the result in the terminal.
# if you want to see the result, in the terminal just uncomment these lines and run the file

# call_binary_search_fun = array_binary_search(sort_array([-131, -82, 0, 27, 42, 68, 179]), 42)
# if call_binary_search_fun != -1:
#     print(str(call_binary_search_fun))
# else:
#     print(-1)

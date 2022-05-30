def reverseList(array, start, end):

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    print(array)
    return array

reverseList([1, 2, 3, 4, 5, 6], 0, 5)




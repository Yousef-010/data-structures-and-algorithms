
def array_insert_shift(array, number):
    mid_arr = int(len(array)/2)
    if len(array) == 0:
        array.append(number)
    elif len(array) % 2 == 0:
        array.insert(mid_arr, number)
    else:
        array.insert(mid_arr+1, number)
    return array





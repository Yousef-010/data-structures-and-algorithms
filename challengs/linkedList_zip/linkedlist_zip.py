from linked_list.linked_list import *


def length_list(first_linked_list, second_linked_list):
    """
    this function to get the size of each linked list
    """
    counter1 = 0
    counter2 = 0
    cur1 = first_linked_list.head
    cur2 = second_linked_list.head
    while cur1:
        counter1 += 1
        cur1 = cur1.next
    while cur2:
        counter2 += 1
        cur2 = cur2.next

    return counter1, counter2


def zip_lists(first_linked_list, second_linked_list):
    """
    this function takes 2 arguments: first_linked_list and second_linked_list as linked lists and return zipped linked list
    with O(1) space complexity.
    Arguments: 2 linked lists
    Return:  Linked Lists zipped
    """

    current1 = first_linked_list.head
    current2 = second_linked_list.head
    f_size = length_list(first_linked_list, second_linked_list)[0]
    s_size = length_list(first_linked_list, second_linked_list)[1]

    while True:
        if current1 is None and current2 is None:
            return 'your linked_lists id empty'

        if current1 is None:
            return second_linked_list

        if current2 is None:
            return first_linked_list

        if f_size == s_size:
            first_linked_list.insert_after(current1.value, current2.value)
            current2 = current2.next
            current1 = current1.next.next
            if current1.next is None:
                first_linked_list.append(current2.value)
                return first_linked_list

        if f_size < s_size:
            second_linked_list.insert_before(current2.value, current1.value)
            current2 = current2.next
            current1 = current1.next
            if current2.next is None:
                return second_linked_list

        if f_size > s_size:
            first_linked_list.insert_after(current1.value, current2.value)
            current2 = current2.next
            current1 = current1.next.next
            if current1.next is None:
                return first_linked_list


if __name__ == "__main__":
    first_linked_list = LinkedList()
    second_linked_list = LinkedList()

    first_linked_list.append(1)
    first_linked_list.append(3)
    first_linked_list.append(2)

    second_linked_list.append(5)
    second_linked_list.append(9)
    second_linked_list.append(4)

    print(zip_lists(first_linked_list, second_linked_list).to_string())

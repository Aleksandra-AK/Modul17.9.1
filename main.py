from List import List
import sys


def find_element(first_node, value):
    position = 0
    print(f"You enter the value: {value}")
    if first_node is None:
        print("List is empty")
        return
    if first_node.next is None:
        print(f"List have single element")
    if value < first_node.value:
        print(f"Entered the value {value} is less minimal value({first_node.value}) of list ")
    else:
        while first_node.next is not None:
            if first_node.next.value >= value:
                return position
            else:
                position += 1
                first_node = first_node.next
    print(f"Entered the value {value} is larger maximal value({first_node.value}) of list")
    return None


def split_list(first_node):
    if first_node is None or first_node.next is None:
        return first_node
    left_start = first_node
    right_start = first_node.next
    while (right_start is not None) and (right_start.next is not None):
        left_start = left_start.next
        right_start = right_start.next.next
    right_start = left_start.next
    left_start.next = None
    left_start = first_node
    # print(right_start)
    # print(first_node)
    return merge_lists(split_list(left_start), split_list(right_start))


def merge_lists(left_first_node, right_first_node):
    result_list = List()
    # print(result_list)
    while (left_first_node is not None) and (right_first_node is not None):
        #     a, b = ,
        # print(f"a={a}, b={b}")
        if left_first_node.value < right_first_node.value:
            result_list.push_right(left_first_node.value)
            left_first_node = left_first_node.next
        else:
            result_list.push_right(right_first_node.value)
            right_first_node = right_first_node.next
    if left_first_node is None:
        result_list.last.next = right_first_node
    else:
        result_list.last.next = left_first_node
    # print(result_list.first)
    return result_list.first


if __name__ == '__main__':
    if len(sys.argv) == 1:
        nodes_values = list(input("Enter numbers separated by a space: ").split(" "))
    else:
        nodes_values = list(sys.argv[1].split(" "))
    list_of_numeric = List()
    for node in nodes_values:
        try:
            list_of_numeric.push_right(int(node))
        except ValueError:
            print(f"The value \"{node}\" does't meet the condition")
            continue
    while True:
        try:
            user_value = int(input("Enter the digit: "))
            break
        except ValueError:
            print("Enter the valid digit")
            continue
    print(f"Entered list of numbers: {list_of_numeric.first}")
    # print(list_of_numeric)
    list_of_numeric = split_list(list_of_numeric.first)
    print(f"Sorted list of numbers: {list_of_numeric}")
    print(f"Find position: {find_element(list_of_numeric, user_value)}")

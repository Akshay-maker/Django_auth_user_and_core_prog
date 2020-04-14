Input = [('z',2), ('y',1), ('z',1), ('a',1), ('b',1), ('a',2), ('f',1)]


def sort_tuple(arr):
    num_list = []
    sorted_list = []
    [num_list.append((ord(elem[0]), elem[1])) for elem in arr]
    num_list.sort(key=lambda a: (a[0], a[1]))
    [sorted_list.append((chr(elem[0]), elem[1])) for elem in num_list]
    return sorted_list


print(sort_tuple(Input))
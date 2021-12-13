def default_cmp(obj1, obj2):
    """

    :param obj1: a
    :param obj2: a
    :return: -1 = a < b ; 0 a == b; 1 = a > b
    """
    return (-1) * int((obj1 < obj2)) + 0 * int(obj1 == obj2) + 1 * int(obj1 > obj2)


def default_key(element):
    return element


def sort(collection, key=default_key, reverse=False, cmp=default_cmp):
    bubble_sort(collection, key, reverse, cmp)


def bubble_sort(collection, key, reverse, cmp):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(collection) - 1):
            compare_result = cmp(key(collection[i]), key(collection[i+1]))
            if reverse:
                if compare_result == -1:
                    collection[i], collection[i+1] = collection[i+1], collection[i]
                    is_sorted = False
                else:
                    if compare_result == 0 or compare_result == 1:
                        collection[i], collection[i + 1] = collection[i + 1], collection[i]
                        is_sorted = False




lst = [9, 8, 7, 6, 5]
sort(lst)
print(lst)


# print(default_cmp(1, 2))
# print(default_cmp(0, 0))
# print(default_cmp(2, 1))

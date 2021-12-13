def default_key(element):
    return element


def sort(collection, key=default_key, reverse=False):
    #bubble_sort(collection, key, reverse)
    shell_sort(collection, key, reverse)


def not_ordered(obj1, obj2, reverse):
    if reverse:
        return obj1 < obj2
    return obj1 > obj2


def bubble_sort(collection, key, reverse):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(collection) - 1):
            if not_ordered(key(collection[i]), key(collection[i + 1]), reverse):
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                is_sorted = False


def shell_sort(collection, key, reverse):
    gap = len(collection) // 2  # initialize the gap
    while gap > 0:
        i = 0
        j = gap
        # check the array in from left to right
        # till the last possible index of j
        while j < len(collection):
            if not_ordered(key(collection[i]), key(collection[j]), reverse):
                collection[i], collection[j] = collection[j], collection[i]
            i += 1
            j += 1
            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            back = i
            while back - gap > -1:
                if not_ordered(key(collection[back - gap]), key(collection[back]), reverse):
                    collection[back - gap], collection[back] = collection[back], collection[back - gap]
                back -= 1
        gap //= 2


lst = [(7, 9), (4, 9), (4, 9), (-20, 7), (7, 9)]
sort(lst, key=lambda x: x[0], reverse=False)
print(lst)

# print(default_cmp(1, 2))
# print(default_cmp(0, 0))
# print(default_cmp(2, 1))

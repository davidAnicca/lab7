import random


def default_key(element):
    return element


def sort(collection, keyy=default_key, cmp=lambda x, y: x < y, reverse=False):
    bubble_sort(collection, keyy, cmp, reverse)
    # shell_sort(collection, key, cmp, reverse)


def not_ordered(obj1, obj2, cmp, reverse):
    if obj1 == obj2:
        return False
    if reverse:
        return cmp(obj1, obj2)
    return not cmp(obj1, obj2)


def bubble_sort(collection, keyy, cmp, reverse):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(collection)-1):
            if not_ordered(keyy(collection[i]), keyy(collection[i + 1]), cmp, reverse):
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                is_sorted = False


def shell_sort(collection, keyy, cmp, reverse):
    gap = len(collection) // 2  # initialize the gap
    while gap > 0:
        i = 0
        j = gap
        # check the array in from left to right
        # till the last possible index of j
        while j < len(collection):
            if not_ordered(keyy(collection[i]), keyy(collection[j]), cmp, reverse):
                collection[i], collection[j] = collection[j], collection[i]
            i += 1
            j += 1
            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            back = i
            while back - gap > -1:
                if not_ordered(keyy(collection[back - gap]), keyy(collection[back]), cmp, reverse):
                    collection[back - gap], collection[back] = collection[back], collection[back - gap]
                back -= 1
        gap //= 2


# test
def test():
    lst = []
    for i in range(10):
        lst.append(random.randint(-100, 100))
    print(lst)
    copy_lst = lst[:]
    copy_lst.sort()
    sort(lst)
    print(lst)
    assert (lst == copy_lst)

    lst.clear()
    for i in range(10):
        lst.append((random.randint(-100, 100), random.randint(-100, 100)))
    print(lst)
    copy_lst = lst[:]
    copy_lst.sort(key=lambda x: x[0])
    sort(lst, keyy=lambda x: x[0])
    print(lst)
    assert (lst == copy_lst)

    copy_lst.sort(key=lambda x: x[1], reverse=True)
    sort(lst, keyy=lambda x: x[1], reverse=True)
    print(lst)
    assert (lst == copy_lst)


test()
# print(default_cmp(1, 2))
# print(default_cmp(0, 0))
# print(default_cmp(2, 1))

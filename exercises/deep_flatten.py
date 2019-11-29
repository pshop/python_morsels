import logging


def deep_flatten(deep_list):
    for elem in deep_list:
        try:
            yield from deep_flatten(elem)
        except TypeError as te:
            yield elem


if __name__ == '__main__':
    list1 = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    list2 = {(1, 2), (3, 4), (5, 6), (7, 8)}
    list3 = [['apple', 'pickle'], ['pear', 'avocado']]

    print([e for e in deep_flatten(list1)])
    print([e for e in deep_flatten(list2)])
    print([e for e in deep_flatten(list3)])




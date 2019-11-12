matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
import copy
from timeit import default_timer as timer

#récupérer le premier elemenet de chaque liste

# def add_two(matrix1=matrix1, matrix2=matrix2):
#     matrix_result = list()
#     for line1, line2 in zip(matrix1, matrix2):
#         matrix_line = list()
#         for elem1, elem2 in zip(line1, line2):
#             matrix_line.append(elem1+elem2)
#         matrix_result.append(matrix_line)
#     print(matrix_result)

def add(*matrix):

    result = copy.deepcopy(matrix[0])
    nb_line = len(result)
    nb_elem_per_line = len(result[0])
    for m in matrix[1:]:
        if nb_line != len(m):
            raise ValueError('Given matrices are not the same size.')
        for i, line in enumerate(m):
            if nb_elem_per_line != len(line):
                raise ValueError('Given matrices are not the same size.')
            for j, num in enumerate(line):
                result[i][j] += num
    return result

def get_shape(matrix):
    return [len(r) for r in matrix]

def add_soluce1(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    shape_of_matrix = get_shape(matrices[0])
    if any(get_shape(m) != shape_of_matrix for m in matrices):
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]

from itertools import zip_longest

def add_soluce2(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    try:
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e



if __name__ == '__main__':
    #add_two()
    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4]]
    m3 = [[2, 1], [3, 4]]
    m4 = [[9, 9], [9, 9]]
    m5 = [[31, 32], [27, 24]]
    #print(add(m1, m2, m3))
    start = timer()
    for _ in range(10000):
        add(m2, m3, m1, m1, m2, m4, m1)
    end = timer()
    print(f"exec1 = {end-start}")

    start = timer()
    for _ in range(10000):
        add_soluce1(m2, m3, m1, m1, m2, m4, m1)
    end = timer()
    print(f"exec2 = {end - start}")

    start = timer()
    for _ in range(10000):
        add_soluce2(m2, m3, m1, m1, m2, m4, m1)
    end = timer()
    print(f"exec3 = {end - start}")




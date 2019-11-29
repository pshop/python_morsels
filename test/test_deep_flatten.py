from exercises.deep_flatten import deep_flatten

first_list = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
first_result = [1, 2, 3, 4, 5, 6, 7, 8]

second_list = [[1, [2, 3]], 4, 5]
second_result = [1, 2, 3, 4, 5]

def test_base_flatten():
    assert [e for e in deep_flatten(first_list)] == first_result
    assert [e for e in deep_flatten(second_list)] == second_result

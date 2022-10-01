# Implement a function that returns a list of odd numbers in order of a desired length

def build_odd_numbers_list(length: int) -> list[int]:
    # implement me
    return []


def test():
    assert build_odd_numbers_list(1) == [0]
    assert build_odd_numbers_list(2) == [0, 2]
    assert build_odd_numbers_list(3) == [0, 2, 4]
    assert build_odd_numbers_list(4) == [0, 2, 4, 6]
    assert build_odd_numbers_list(10) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


test()

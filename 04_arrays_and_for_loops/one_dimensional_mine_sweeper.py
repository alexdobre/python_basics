# In the game mine sweeper the grid contains mines and the cells next to the mains contain a number equal to how many
# mines are neighbors.
# In our first example we will take a simpler version of just an array.
# Given a non-empty array where mines are -1, build the array by filling in the right numbers in neighboring cells.


def populate_array(ar: list[int]) -> list[int]:
    # implement me
    return ar


def test():
    assert populate_array([-1]) == [-1]
    assert populate_array([0, -1, 0]) == [1, -1, 1]
    assert populate_array([-1, 0, 0]) == [-1, 1, 0]
    assert populate_array([0, 0, -1]) == [0, 1, -1]
    assert populate_array([0, 0, -1, -1, 0, 0]) == [0, 1, -1, -1, 1, 0]
    assert populate_array([0, 0, -1, 0, -1, 0]) == [0, 1, -1, 2, -1, 1]
    assert populate_array([0, 0, -1, 0, -1, 0, 0, 0, -1, -1, 0, -1]) == [0, 1, -1, 2, -1, 1, 0, 1, -1, -1, 2, -1]


test()

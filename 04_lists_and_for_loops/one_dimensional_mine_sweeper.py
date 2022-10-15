# In the game mine sweeper the grid contains mines and the cells next to the mains contain a number equal to how many
# mines are neighbors.
# In our first example we will take a simpler version of just an array.
# Given a non-empty array where mines are -1, build the array by filling in the right numbers in neighboring cells.


def populate_array(ar: list[int]) -> list[int]:
    for index, x in enumerate(ar):
        if x == -1:
            continue
        if index == 0:  # we are at the beginning of the array
            neighbour_to_the_left = 0
        else:
            neighbour_to_the_left = ar[index - 1]

        if index == len(ar) - 1:  # we are at the end of the array
            neighbour_to_the_right = 0
        else:
            neighbour_to_the_right = ar[index + 1]

        if neighbour_to_the_left == -1:
            ar[index] += 1
        if neighbour_to_the_right == -1:
            ar[index] += 1

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

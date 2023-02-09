# The core rule for the game Mine Sweeper is that for each cell that is not a mine, the number in the cell is equal to the number of mines this cell neighbours.

# Two cells are considered neighbours if they are next to each other vertically, horizontally or diagonally.

# Given an input grid of integers where the mines are represented as -1 and empty cells are represented as 0, implement the generateGrid method in the class below.

# We consider a rectangular non empty matrix as the input.


class MineSweeperGrid:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.generate_grid()

    def get_grid(self) -> list[list[int]]:
        return self.grid

    def generate_grid(self) -> None:
        # implement me
        return


def test():
    assert [
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]
           ] == MineSweeperGrid([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]).get_grid(), 'Empty grid'

    assert MineSweeperGrid([
        [-1, 0, 0, 0, -1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [-1, 0, 0, 0, -1]
    ]).get_grid() == [
               [-1, 1, 0, 1, -1],
               [1, 1, 0, 1, 1],
               [1, 1, 0, 1, 1],
               [-1, 1, 0, 1, -1]
           ], 'Mines in corners'

    assert MineSweeperGrid([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, -1, -1, 0, 0],
        [0, 0, -1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]).get_grid() == [
               [0, 0, 0, 0, 0, 0],
               [0, 1, 2, 2, 1, 0],
               [0, 2, -1, -1, 2, 0],
               [0, 2, -1, -1, 2, 0],
               [0, 1, 2, 2, 1, 0],
               [0, 0, 0, 0, 0, 0]
           ], 'Cluster in center'

    assert MineSweeperGrid([
        [0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, 0],
        [0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, 0],
        [0, -1, 0, -1, 0, -1],
        [-1, 0, -1, 0, -1, 0],
    ]).get_grid() == [
               [2, -1, 3, -1, 3, -1],
               [-1, 4, -1, 4, -1, 3],
               [3, -1, 4, -1, 4, -1],
               [-1, 4, -1, 4, -1, 3],
               [3, -1, 4, -1, 4, -1],
               [-1, 3, -1, 3, -1, 2],
           ], 'Checquer'

    assert MineSweeperGrid([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, -1, -1, -1, 0, 0],
        [0, -1, 0, -1, 0, 0],
        [0, -1, -1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]).get_grid() == [
               [0, 0, 0, 0, 0, 0],
               [1, 2, 3, 2, 1, 0],
               [2, -1, -1, -1, 2, 0],
               [3, -1, 8, -1, 3, 0],
               [2, -1, -1, -1, 2, 0],
               [1, 2, 3, 2, 1, 0]
           ], 'Square'

    assert MineSweeperGrid([
        [0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0],
        [0, -1, 0, 0, -1, 0],
        [0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0]
    ]).get_grid() == [
               [1, 1, 1, 0, 0, 0],
               [2, -1, 2, 1, 1, 1],
               [2, -1, 2, 1, -1, 2],
               [1, 1, 1, 1, 2, -1],
               [0, 1, 1, 1, 1, 1],
               [0, 1, -1, 1, 0, 0]
           ], 'Random1'

    assert MineSweeperGrid([
        [0, 0, 0, 0, -1, 0],
        [0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, -1, -1, 0, 0, 0],
        [0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]).get_grid() == [
               [0, 0, 1, 2, -1, 1],
               [0, 0, 1, -1, 2, 1],
               [1, 2, 3, 2, 1, 0],
               [1, -1, -1, 2, 0, 0],
               [1, 3, -1, 2, 0, 0],
               [0, 1, 1, 1, 0, 0]
           ], 'Random2'

    print('All tests passed!')


test()
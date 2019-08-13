"""
rows = 6
columns = 4
bombs = 2

1   1   1   0
1   -1  1   0
1   2   2   1
0   1   -1  1
0   1   1   1
0   0   0   0

"""

import random

def pick_one_position(rows, columns, bombs):
    i = random.choice(range(rows))
    j = random.choice(range(columns))
    return [i, j]


def get_positions(rows, columns, bombs):
    positions = []

    for _ in range(bombs):
        p = pick_one_position(rows, columns, bombs)
        while len(positions) < bombs and p not in positions:
            positions.append(p)

    return positions


def gen_matrix(rows, columns, bombs):

    # initialize matrix with 0's
    matrix = []
    for _ in range(rows):
        matrix.append([0 for _ in range(columns)])

    # TODO:  fill in non-0 cells
    #

    return matrix

if __name__ == '__main__':
    positions = get_positions(6,4,2)
    print(positions)

    m = gen_matrix(6,4,2)
    print(m)


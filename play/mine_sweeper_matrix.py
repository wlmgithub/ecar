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

    # fill bomb positions
    for position in get_positions(rows, columns, bombs):
        i, j = position
        matrix[i][j] = -1

    print('1-------: ', matrix)


#####
#
# https://github.com/Lintik/CodeFights-Arcade/tree/master/Intro/Island%20of%20Knowledge/Minesweeper
#
# https://knaidu.gitbooks.io/problem-solving/matrix/matrix/minesweeper.html
#
    r = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
    # TODO:  fill in non-0 cells
    #
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    try:
                        if a < 0 or b < 0:
                            continue
                        if matrix[i][j]:
                            r[a][b] += 1
                    except:
                        continue
            if matrix[i][j]: r[i][j] -= 1
    return r


    return matrix

if __name__ == '__main__':
    positions = get_positions(6,4,2)
    print(positions)

    m = gen_matrix(6,4,2)
    print(m)


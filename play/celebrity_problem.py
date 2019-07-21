
# https://www.sanfoundry.com/python-program-solve-celebrity-problem/

def get_possible_celeb(matrix):
    """Take an n x n matrix that has m[i][j] = True iff i knows j and return
    person who is maybe a celebrity."""
    possible_celeb = 0
    for p in range(1, len(matrix)):
        if (matrix[possible_celeb][p]
            or not matrix[p][possible_celeb]):
            possible_celeb = p
    return possible_celeb


def check_if_celeb(possible_celeb, matrix):
    """Take an n x n matrix that has m[i][j] = True iff i knows j and return
    True if possible_celeb is a celebrity."""
    for i in range(len(matrix)):
        if matrix[possible_celeb][i] is True:
            return False

    for i in range(len(matrix)):
        if matrix[i][possible_celeb] is False:
            if i != possible_celeb:
                return False

    return True


if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0],
    ]


    matrix = [
        [False, True],
        [True, False]
    ]

    matrix = [
        [0]
    ]

    matrix = [
        [0,1],
        [1,0]
    ]

#    matrix = [
#        [1,0,1,1,0,0],
#        [1,1,1,1,0,0],
#        [0,1,0,1,1,0],
#        [0,0,0,0,0,0],
#        [1,1,1,1,1,1],
#        [0,0,0,1,0,0]
#    ]

    matrix = [
        [True, False, True, True, False, False],
        [True, True, True, True, False, False],
        [False, True, False, True, True, False],
        [False, False, False, False, False, False],
        [True, True, True, True, True, True],
        [False, False, False, True, False, False]
        ]

    print(matrix)


    possible_celeb = get_possible_celeb(matrix)

    if check_if_celeb(possible_celeb, matrix):
        print(f'{possible_celeb} is celeb')
    else:
        print('no celeb found')


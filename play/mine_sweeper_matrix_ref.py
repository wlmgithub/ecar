
def minesweeper(matrix):
    r = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
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


matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

print(matrix)
print(minesweeper(matrix))

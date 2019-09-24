
# https://colorfulcodesblog.wordpress.com/2018/09/06/number-of-islands-tutorial-python/

def num_islands(graph):
    if not graph:
        return 0

    row = len(graph)
    col = len(graph[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                dfs(graph, row, col, i, j)
                count += 1

    return count

def dfs(graph, row, col, x, y):

    if graph[x][y] == 0:
        return
    graph[x][y] = 0

    if x != 0:
        dfs(graph, row, col, x-1, y)
    if x != row - 1:
        dfs(graph, row, col, x+1, y)
    if y != 0:
        dfs(graph, row, col, x, y-1)
    if y != col - 1:
        dfs(graph, row, col, x, y+1)


if __name__ == '__main__':
    graph = [
    [1,1,0,0,0],
    [0,1,0,0,1],
    [1,0,0,1,1],
    [0,0,0,0,0],

    ]

    print(graph)
    print(num_islands(graph))


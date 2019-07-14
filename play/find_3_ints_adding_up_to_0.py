
def find_triplets(A):
    n = len(A)

    found = False
    for i in range(0, n-2) :
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if A[i] + A[j] + A[k] == 0:
                    print(A[i], A[j], A[k])
                    found = True

    if not found:
        print('not exists')

arr = [0, -1, 2, -3, 1]
#arr = [1,2,3,4]
find_triplets(arr)

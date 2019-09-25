#import heapq

A = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]

print(A)


def mergeit(A, B):
    res = []
    while A and B:
        if A[0] < B[0]:
            res.append(A.pop(0))
        else:
            res.append(B.pop(0))
    return res + A + B

def sortit(A):
    res = []
    for a in A:
        res = mergeit(res, a)

    return res

r = sortit(A)
print(r)



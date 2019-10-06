
def search_smallest(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left

def search_largest(A):
    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left - 1

A = [7,8,9,10,1,2,3,4,5]
#A = [4,5,1,2,3]

assert search_smallest(A) == 4
assert search_largest(A) == 3

"""
Maximum difference between two elements such that larger element appears after the smaller number

https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
"""
def find_max_diff(A):
    alen = len(A)
    max_diff = A[1] - A[0]
    min_elem = A[0]

    for i in range(1, alen):
        if A[i] - min_elem > max_diff:
            max_diff = A[i] - min_elem

        if A[i] < min_elem:
            min_elem = A[i]

    return max_diff


if __name__ == '__main__':
    A = [7, 9, 5, 6, 3, 2]
    A = [2, 3, 10, 6, 4, 8, 1]
    print(A)
   res = find_max_diff(A)
    print(res)

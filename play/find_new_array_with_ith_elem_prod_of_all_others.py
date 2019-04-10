
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


import functools


def get_product(A):
    return functools.reduce(lambda x, y: x * y, A)


def get_result(A):
    if len(A) < 2:
        return A

    res = []
    for i, n in enumerate(A):
            r = get_product(A[:i] + A[i+1:])
    #        print(i, r)
            res.append(r)
    #        print('3====: ', i, r)
   
    return res

        
if __name__ == '__main__':
    A = [3,2,1]
    A = [1, 2, 3, 4, 5]
    result = get_result(A)

    print(A)
    print(result)

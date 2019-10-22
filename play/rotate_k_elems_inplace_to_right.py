'''
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.
'''


def rotate(A, k):
    
    def rotate_one(A, k, src_ind, src_num, count=0):
        if count == len(A):
            return 
    
        dest_ind = ( src_ind + k ) % len(A)
        dest_num = A[dest_ind]
    
        A[dest_ind] = src_num
    
        rotate_one(A, k, dest_ind, dest_num, count + 1)
    
    if k < 1:
        return A

    rotate_one(A, k, 0, A[0])



A = [1,2,3]

rotate(A,0)
assert A == [1,2,3]

rotate(A,1)
assert A == [3,1,2]

rotate(A,2)
assert A == [1,2,3]







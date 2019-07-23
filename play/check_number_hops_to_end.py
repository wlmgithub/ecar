"""
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

A = [2,0,1,0] # ok
A = [1,1,0,1] # not

A = [3,0,0,2,1,6]  # ok



i = 0
idx = 0
while i < len(A)-1:
    print(i, end=' ')
    idx += A[i]

    if idx == i:
        break

    i = idx
    print( idx, end='\n')

if i == len(A)-1:
    print('OK')
else:
    print('not OK')

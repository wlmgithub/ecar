

def testme(A, K):
    if len(A) < 2:
        return False

    # len(A) >= 2
    for i, n in enumerate(A):
        rest = A[:i] + A[i+1:]
        s = K - n
        print(i, n, s, rest)
        if s in rest:
            return True
    return False

def find_indexes(A, K):
	hash_table = {}
	for i, num in enumerate(A):
	    if K - num in hash_table:
	        return([hash_table[K - num], i])
	        break
	    hash_table[num] = i
	return([])

if __name__ == '__main__':

    # For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    A = [10, 15, 3, 7]
    K = 17

    A = [10,2,1,11]
    K = 20

    A = [10, 15, 3, 7]
    K = 10

    print(f'A: {A}\nK: {K}\n')
    res = testme(A, K)
    print(res)
    print(find_indexes(A, K))

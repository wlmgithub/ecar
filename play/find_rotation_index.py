
def findit(A):
    if len(A) <= 1:
        return 0
    if len(A) == 2:
        if A[0] <= A[1]:
            return 0
        else:
            return 1

    # len(A) > 2
    for i, w in enumerate(A):
        if w > A[i+1]:
            return i+1
        
    


if __name__ =='__main__':

    words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

    print(words)
    res = findit(words)
    print(res)


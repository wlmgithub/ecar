#
# https://www.algorithmist.com/index.php/Longest_Common_Subsequence
#

def lcs3(a, b):
    # generate matrix of length of longest common subsequence for substrings of both words
    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    # read a substring from the matrix
    result = ''
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += a[i-1]

    return lengths[len(a)][len(b)], result

def lcs2(x, y):
    n = len(x)
    m = len(y)
    table = dict()  # a hashtable, but we'll use it as a 2D array here

    for i in range(n+1):     # i=0,1,...,n
        for j in range(m+1):  # j=0,1,...,m
            if i == 0 or j == 0:
                table[i, j] = 0
            elif x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i-1, j], table[i, j-1])

    # Now, table[n, m] is the length of LCS of x and y.

    # Let's go one step further and reconstruct
    # the actual sequence from DP table:

    def recon(i, j):
        if i == 0 or j == 0:
            return []
        elif x[i-1] == y[j-1]:
            return recon(i-1, j-1) + [x[i-1]]
        elif table[i-1, j] > table[i, j-1]: #index out of bounds bug here: what if the first elements in the sequences aren't equal
            return recon(i-1, j)
        else:
            return recon(i, j-1)

    return table[n, m], recon(n, m)

def lcs(s1: str, s2: str):
    # rows -> s1 , cols -> s2
    rows = len(s1) + 1
    cols = len(s2) + 1

    # row0 and col0 will be 0 as they will signify null strings
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):

            # if the chars match, go for left-top diagonal value + 1
            if s1[i - 1] == s2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            # otherwise get max of top or left
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

    # length of longest common sub-sequence
    # return dp_array[rows-1][cols-1]

    # store the common sequence (will be stored in reverse)
    sub_sequence = []

    i = rows - 1
    j = cols - 1

    # find the lcs
    while i > 0 and j > 0:
        # if top is not equal, that means present char was used
        if dp_array[i][j] != dp_array[i - 1][j]:
            sub_sequence.append(s1[i - 1])
            i -= 1
            j -= 1
        # not used
        else:
            i -= 1

    # return length of lcs, list of char containing the lcs elements
    return dp_array[rows - 1][cols - 1], sub_sequence[::-1]

# main
if __name__ == "__main__":
    print("Enter input, e.g., AAA BBBBB")
    s1, s2 = input().split()

    max_lcs, sequence = lcs(s1, s2)

    print("Length of longest common sub-sequence")
    print(max_lcs)
    print("Longest commmon sub-sequence")
    print(''.join(sequence))

    print('************************************************************ lcs2 ')
    max_lcs, sequence = lcs2(s1, s2)

    print("Length of longest common sub-sequence")
    print(max_lcs)
    print("Longest commmon sub-sequence")
    print(''.join(sequence))
    print('************************************************************ lcs3 ')
    max_lcs, sequence = lcs3(s1, s2)

    print("Length of longest common sub-sequence")
    print(max_lcs)
    print("Longest commmon sub-sequence")
    print(''.join(sequence))

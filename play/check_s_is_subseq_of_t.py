
s, t = "abc", "ahbgdc"
s, t = "axc" , "ahbgdc"
s,t = ['x', 'a', 'c', 'b'], ['z', 'x','a', 'c', 'b', 'e', 'k']


def testit(s, t):
    if not s:
        return True

    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


print(s, t, testit(s, t))


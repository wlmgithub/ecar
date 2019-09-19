# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/382379/Python3-regex-find
import re

s = '(abcd)'
s = '(u(love)i)'
s = "(ed(et(oc))el)"
s = "a(bcdefghijkl(mno)p)q"

def doit(s):
    while '(' in s:
        posopen = s.rfind('(')
        print(f'posopen: {posopen}')
        #posclose = s.find(')', posopen+1)
        posclose = s.find(')')  # this should suffice
        print(f'posclose: {posclose}')
        s = s[:posopen] + s[posopen+1:posclose][::-1] + s[posclose+1:]
        print(s)
    return s

print(s, doit(s))

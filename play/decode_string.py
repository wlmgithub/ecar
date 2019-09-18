import re

def decodeString(s):
    pattern =r"(\d+)\[([a-zA-Z]+)\]"
    match = re.search(pattern,s)
    while match is not None:
        num,alpha = match.groups()
        s = s[:match.start()] + alpha * int(num) + s[match.end():]
        match = re.search(pattern,s)
    return s


s = "2[abc]3[cd]ef"
s = "3[a]2[bc]"
s = "3[a2[c]]"

print(s, decodeString(s))

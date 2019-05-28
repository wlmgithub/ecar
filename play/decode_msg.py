
def doit(s):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    Examples:
    >>> coding_problem_7('111')  # possible interpretations: 'aaa', 'ka', 'ak'
    3
    >>> coding_problem_7('2626')  # 'zz', 'zbf', 'bfz', 'bfbf'
    4
    """
    if not s:
        return 1

    symbols = map(str, range(1,27))
    matches =  filter(lambda symbol: s.startswith(symbol),  symbols)
    encodings = [doit(s[len(m):]) for m in matches]

    return sum(encodings)


s = '111'
s = '2525'
s = '4322211'
print(s, doit(s))

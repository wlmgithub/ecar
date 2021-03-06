#char_map = {}
#char_map['1'] = 'a'
#char_map['2'] = 'b'
#char_map['3'] = 'c'
#char_map['4'] = 'd'
#char_map['5'] = 'e'
#char_map['6'] = 'f'
#char_map['7'] = 'g'
#char_map['8'] = 'h'
#char_map['9'] = 'i'
#char_map['10'] = 'j'
#char_map['11'] = 'k'
#char_map['12'] = 'l'
#char_map['13'] = 'm'
#char_map['14'] = 'n'
#char_map['15'] = 'o'
#char_map['16'] = 'p'
#char_map['17'] = 'q'
#char_map['18'] = 'r'
#char_map['19'] = 's'
#char_map['20'] = 't'
#char_map['21'] = 'u'
#char_map['22'] = 'v'
#char_map['23'] = 'w'
#char_map['24'] = 'x'
#char_map['25'] = 'y'
#char_map['26'] = 'z'

keys = [str(n) for n in range(1,27)]
print(keys)

vals = [chr(n) for n in range(97,123)]
print(vals)

char_map = dict(zip(keys, vals))
print(char_map)

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


memo_dict = {} # stores the 'code => key' and 'number of ways => value' eg. '11'=> 2 ways(aa,k)
def count_ways(s):
    str_len = len(s)
    if s in memo_dict:
        return memo_dict[s]

    if str_len == 0:
        return 1

    if s[0] == '0':
        return 0


    if str_len > 0 and s[0] in char_map:
        memo_dict[s] = count_ways(s[1:])
    if str_len > 1 and s[:2] in char_map:
        memo_dict[s] += count_ways(s[2:])

    return memo_dict[s]

s = '111'
s = '2525'
s = '4322211'
print(s, doit(s))
print(s, count_ways(s))


# https://stackoverflow.com/questions/8181513/finding-and-grouping-anagrams-by-python

import itertools

s = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = ['az', 'b', 'za']
res = [ list(v) for k, v in itertools.groupby(sorted(s, key=sorted), key=sorted) ]

print(res)

## using defaultdict
import collections
def group_anagrams(given_list):
    m = collections.defaultdict(list)

    for s in given_list:
        m[tuple(sorted(s))].append(s)

    return list(m.values())

print(group_anagrams(s))

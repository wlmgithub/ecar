# https://leetcode.com/problems/critical-connections-in-a-network/

import collections

cons = [[0,1],[1,2],[2,0],[1,3], [0,4]]

d = collections.defaultdict(int)

for c in cons:
    print(c)
    d[c[0]] += 1
    d[c[1]] += 1

print(d)

results = [ k for k in d if d[k] < 2]

print(results)

for res in results:
    pos = [x for x in cons if res in x]
    print(pos)


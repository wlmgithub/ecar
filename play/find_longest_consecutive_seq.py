# https://stackoverflow.com/questions/8664708/in-python-how-does-one-efficiently-find-the-largest-consecutive-set-of-numbers 

s = [1,4,2,3,5,4,5,6,7,8,1,3,4,5,9,10,11,42]
s = [100,4,200,2,1,3]
s  = [ 20,55,9,6,8,7]
maxrun = -1
rl = {}
for x in s:
    run = rl[x] = rl.get(x-1, 0) + 1
    print x-run+1, 'to', x
    if run > maxrun:
        maxend, maxrun = x, run
print(s)
print range(maxend-maxrun+1, maxend+1)


# https://leetcode.com/problems/longest-consecutive-sequence/discuss/330586/python3-O(N)-clean-code

def findit(s):
    if not s:
        return 0

    res = set()
    s = set(s)
    print('---s', s)
    def query(x):
        if x-1 not in s:
            return 1
        print('---', x, x-1)
        res.add(x)
        res.add(x-1)
        return 1 + query(x-1)

    return max(query(x) for x in s), res

print(findit(s))
            

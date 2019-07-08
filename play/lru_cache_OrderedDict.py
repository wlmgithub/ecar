
# https://www.kunxi.org/2014/05/lru-cache-in-python/

import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


def testme():
    c = LRUCache(2)
    c.set('a', 3)
    c.set('b', 2)
    print(c.cache)
    print(c.get('a'))
    c.set('c', 1)
    print(c.get('d'))
    print(c.cache)



if __name__ == '__main__':
    testme()


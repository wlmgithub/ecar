
# https://stackoverflow.com/questions/31522450/find-the-year-with-the-most-number-of-people-alive-in-python

from collections import Counter
from itertools import chain


def most_pop(pop):
    pop_flat = chain.from_iterable(range(i, j+1) for i, j in pop)
    print(pop_flat)
    return Counter(pop_flat).most_common()


if __name__ == '__main__':
    people = [(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939)]
    people = [(1,9), (3,6), (4,7), (5,8)]
    print(most_pop(people)[0])


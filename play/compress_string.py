"""
Given a string, compress it.
e.g., given 'aaabbgddggg', compress it into: 'a3b2g1d2g3'
"""
__author__ = "Liming Wang"
__credits__ = ["Thanks Casey for the question!"]

import itertools

def _compress_using_groupby(given_string):
    group = itertools.groupby(given_string)

    return ''.join(
        [f'{letter}{len(list(it))}' for letter, it in group]
        )

def _compress(given_string):
    count = 0
    ref = given_string[0]
    out_string = ref

    for i in given_string:
        if i == ref:
            count += 1
        else:
            out_string += str(count) + i
            ref = i
            count = 1

    out_string += str(count)

    return out_string


def _testme():
    for func in (_compress, _compress_using_groupby):
        given_string = 'aaabbgddggg'
        out_string = func(given_string)
        print(f'------ testing using: {func.__name__}')
        print(f'given_string: {given_string}')
        print(f'out_string: {out_string}')


if __name__ == '__main__':
    _testme()

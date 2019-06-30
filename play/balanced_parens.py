
import sys

mapping = {
    '[': ']',
    '{': '}',
    '(': ')',
}

def is_balanced(s):
    stack = []
    for x in s:
        if x in mapping:
            stack.append(x)
        else:
            if x in mapping.values() and x != mapping[stack.pop()]:
                return False
    return True


if __name__ == '__main__':
    #s = 'a{[()]}'
    print(mapping)
    s = input('Gimme a str: ')
    print(s)
    print(is_balanced(s))

s = 'apple'

def is_vowel(x):
    return x in ('a', 'e', 'i', 'o', 'u')

def swap_it(s):
    i, j = 0, len(s) - 1
    while i < j:
        if is_vowel(s[i]) and is_vowel(s[j]):
            print(i, j)
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif is_vowel(s[i]) and not is_vowel(s[j]):
            j -= 1
        elif not is_vowel(s[i]) and is_vowel(s[j]):
            i += 1
        else:
            i += 1
            j -= 1
    return ''.join(s)


print(s)
print(swap_it(list(s)))

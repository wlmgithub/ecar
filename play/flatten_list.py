
def flatten(seq):
    r = []
    for x in seq:
        if type(x) == list:
            r += flatten(x)
        else:
            r.append(x)
    return r



seq = [1,[2,3],4]
seq = [1,[2,[5,6],3],4]

print(seq, '-->', flatten(seq))

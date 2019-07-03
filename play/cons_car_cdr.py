def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

"""
def cons(x,y):
  return lambda pick: x if pick == 1 else y
"""

def car(f):
  return f(lambda a, b: a)

def cdr(f):
  return f(lambda a, b: b)

x1 = car(cons(3,4))
print(x1)

x2 = cdr(cons(3,4))
print(x2)


def doit_math(x, y, b):
    return x*b + y*(1 - b)

def doit_bit(x, y, b):
   b = -b
   return ( x & b ) | ( y & ~b )

if __name__ == '__main__':
    x = input('x = ')
    y = input('y = ')
    b = input('b = ')
    x = int(x)
    y = int(y)
    b = int(b)

    print(x, y, b, doit_bit(x, y, b))
    print(x, y, b, doit_math(x, y, b))



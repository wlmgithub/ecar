#!/usr/bin/env python3

def gen_pascal_triangle(n):
    a=[]
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        a[i].append(1)
    return a

def _print(A):
    n = len(A)
    for i in range(n):
        print("   "*(n-i),end=" ",sep=" ")
        for j in range(0,i+1):
            print('{:5}'.format(A[i][j]), end=' ')
        print()


def main():
    n=int(input("Enter number of rows: "))
    pascal_triangle = gen_pascal_triangle(n)
    print(pascal_triangle)
    _print(pascal_triangle)
    
if __name__ == '__main__':
    main()

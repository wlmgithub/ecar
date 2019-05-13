# credit: https://www.hackerrank.com/challenges/ctci-find-the-running-median/forum

import statistics

from bisect import insort
import random 

def use_statistics():
    data1 = [2, 1, 5, 7, 2, 0, 5]

    print(data1)
    for i in range(len(data1) + 1):
        data = data1[:i:]
        if data:
            print( statistics.median(data))


def median(a):
    if len(a)%2==0:
        l=a[len(a)//2 - 1 ];r=a[(len(a)//2) ]
        med=(l+r)/2.0
        
    elif len(a)%2 !=0:
        med=a[len(a)//2]
    return med


if __name__ =='__main__':
    print("Using statistics module:")
    use_statistics()

    print("Using bisect.insort:")
    mylist = random.sample(range(10), 7)
    print(mylist)
    heap=[]
    for i in mylist:
        insort(heap, i)
        print(heap)
        print(median(heap))
"""     for _ in range(int(input())):
        insort(heap,int(input()))
        print(float(median(heap))) """

def heapify(seq):
    for i in reversed(range(1, len(seq))):
        parent = (i - 1) // 2
        if seq[i] < seq[parent]:
            seq[i], seq[parent] = seq[parent], seq[i]

def heapsort(array):
    res = []
    seq = list(array)
    while seq:
        heapify(seq)
        print(seq)
        res.append(seq.pop(0))

    return res

def quick_sort(array):
    if len(array) < 2:
        return array

    pivot = array[0]

    left, right = [], []

    for n in array:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


if __name__ == '__main__':
    import random
    data = random.sample(range(-100,101), 10)
    print("data:		", data)
    sorted_data = heapsort(data)
    print("sorted data:	", sorted_data)

    sorted_data = quick_sort(data)
    print("quick sorted data:	", sorted_data)



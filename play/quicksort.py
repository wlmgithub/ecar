def quick_sort_0(array):
    if len(array) < 2:
        return array

    pivot = array[0]

    left, middle, right = [], [], []

    for n in array:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            middle.append(n)
    left = quick_sort_0(left)
    right = quick_sort_0(right)

    return left + middle + right

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
    sorted_data = quick_sort_0(data)
    print("sorted data:	", sorted_data)
    sorted_data = quick_sort(data)
    print("sorted data:	", sorted_data)

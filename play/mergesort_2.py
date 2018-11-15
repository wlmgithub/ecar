
def merge(left, right):
    """Merge sort merging function."""

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


if __name__ == '__main__':
    import random
    data = random.sample(range(1,101), 10)
    print("data:		", data)
    sorted_data = merge_sort(data)
    print("sorted data:	", sorted_data)



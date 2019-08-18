"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

dp = []
def findit(arr):
    print(arr)
    for i in range(len(arr)):
        print(i, arr[i])
    dp = arr[:]
    res = 0

    for i in range(1, len(arr)):
        dp[i] = max(dp[i-1], 0) + arr[i]
        res = max(res, dp[i])

    return res

if __name__ == '__main__':
    A = [34, -50, 42, 14, -5, 86]
    A = [-5, -1, -8, -9]
    print(A, findit(A))

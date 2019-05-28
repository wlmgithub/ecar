"""
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

prices = [9, 11, 8, 5, 7, 10]

def findit(A):
    max_profit = 0
    max_future_price = 0
    for i  in range(len(A) -1, 0, -1):
       max_future_price = max(max_future_price, A[i])
       max_profit = max(max_profit, max_future_price - A[i-1])
    return max_profit

print(prices, findit(prices))

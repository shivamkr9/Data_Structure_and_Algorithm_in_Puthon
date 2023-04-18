"""

You are given an array of prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Input: prices = [7,1,5,3,6,4]	Output: 5
Input: prices = [7,6,4,3,1]	Output: 0

"""
from typing import List


def getMaxProfit(li: List) -> int:
    profit: int = 0
    for i in range(0, len(li)):
        for j in range(i + 1, len(li)):
            calc = li[j] - li[i]
            if calc > profit:
                profit = calc
    return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 2, 6, 4, 1]
    print(getMaxProfit(prices))

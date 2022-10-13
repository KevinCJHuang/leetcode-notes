<!-- 
Coin Change (https://leetcode.com/problems/coin-change/)
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin. -->


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        minCounts = []
        for i in range(amount + 1):
            minCount = sys.maxsize
            for coin in coins:
                if (i - coin) >= 0:
                    if minCounts[i - coin] == -1:
                        curMin = 1 if (i) % coin == 0 else -1
                    else:
                        curMin = minCounts[i-coin] + 1
                    minCount = min(minCount, curMin) if curMin != -1 else minCount
            minCounts.append(minCount if minCount != sys.maxsize else -1)
        return minCounts[amount]
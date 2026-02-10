# NeetCode - Sliding Window
# 121. Best Time to Buy And Sell Stock (Easy)
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    # 시간복잡도 O(N^2)
    # 공간복잡도 O(N)
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                result = max(prices[j] - prices[i], result)

        return result

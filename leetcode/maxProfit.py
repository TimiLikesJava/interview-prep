class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_N = 0
        
        i = 0
        for j in range(1 , len(prices)):
            if prices[i] >= prices[j]:
                i = j
            else:
                diff = prices[j] - prices[i]
                if diff > max_N:
                    max_N = diff
        return max_N

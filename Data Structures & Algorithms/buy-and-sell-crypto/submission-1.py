class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        
        for i in range(n):
            for j in range(i + 1, n): 
                best = max(best, prices[j] - prices[i])
        
        return best
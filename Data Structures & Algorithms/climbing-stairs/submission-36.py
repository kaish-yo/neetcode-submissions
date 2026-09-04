class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def dfs(i):
            # Base cases
            if i > n:
                return 0
            if i == n:
                return 1
            
            # Recurring cases
            if not i + 1 in memo:
                memo[i + 1] = dfs(i + 1)
            if not i + 2 in memo:
                memo[i + 2] = dfs(i + 2)
            
            return memo[i + 1] + memo[i + 2]
        
        return dfs(0)

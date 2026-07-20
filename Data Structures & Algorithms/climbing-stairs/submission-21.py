class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(i):
            if i >= n:
                return i == n
            if i + 1 not in memo:
                memo[i + 1] = dfs(i + 1)
            if i + 2 not in memo:
                memo[i + 2] = dfs(i + 2)
            return memo[i + 1] + memo[i + 2]

        return dfs(0)

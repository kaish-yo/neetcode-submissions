class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        
        memo = {}

        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            memo[(i + 1, j)] = dfs(i + 1, j)
            memo[(i, j + 1)] = dfs(i, j + 1)
            
            return max(memo[(i + 1, j)], memo[(i, j + 1)])

        return dfs(0, 0)
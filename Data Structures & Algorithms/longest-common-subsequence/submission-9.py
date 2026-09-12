class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        below = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            curr = [0] * (len(text2) + 1 )

            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + below[j + 1]
                else:
                    curr[j] = max(curr[j + 1], below[j])

            below = curr

        return below[0]      
            

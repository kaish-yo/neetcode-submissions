class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 短い方を内側ループにして省メモリ
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0  # dp[i+1][j+1] の退避用
            for j in range(len(text2) - 1, -1, -1):
                temp = dp[j]          # dp[i+1][j] を退避（次のjでprevになる）
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev  # 1 + dp[i+1][j+1]
                else:
                    dp[j] = max(dp[j], dp[j + 1])  # max(dp[i+1][j], dp[i][j+1])
                prev = temp
        
        return dp[0]
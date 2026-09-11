class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        below = [0] * (n + 1)          # i+1 行（1つ下の行）

        for i in range(m - 1, -1, -1):
            cur = [0] * (n + 1)        # 今計算中の i 行

            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = 1 + below[j + 1]
                else:
                    cur[j] = max(below[j], cur[j + 1])

            below = cur                # 次のループでは下の行になる

        return below[0]
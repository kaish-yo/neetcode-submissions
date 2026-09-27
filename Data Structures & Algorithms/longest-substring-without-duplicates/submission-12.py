class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l, r = 0, 0
        best = 0

        for i in range(len(s)):
            while s[i] in c:
                c.remove(s[l])
                l += 1
            c.add(s[i])
            best = max(best, r - l + 1)
            r += 1
        
        return best
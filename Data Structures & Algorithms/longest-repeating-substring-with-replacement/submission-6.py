class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars_count = defaultdict(int)
        l = 0
        max_f = 0
        res = 0

        for r in range(len(s)):
            chars_count[s[r]] += 1
            max_f = max(max_f, chars_count[s[r]])

            if (r - l + 1) - max_f > k:
                chars_count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
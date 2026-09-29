class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = defaultdict(int)
        max_f = 0
        l = 0
        res = 0
        
        for r in range(len(s)):
            char_counts[s[r]] += 1
            max_f = max(max_f, char_counts[s[r]])

            if (r - l + 1) - max_f > k:
                char_counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
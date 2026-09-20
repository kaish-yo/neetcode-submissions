class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        best = curr = 0
        for i, x in enumerate(s):
            curr = curr + 1 if i and x == s[i-1] + 1 else 1
            best = max(best, curr)
        return best
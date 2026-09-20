class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        if len(nums) == 0:
            return 0
            
        nums_ = sorted(set(nums))
        length = len(nums_)

        dp = [1] * length

        curr = 1
        for i in range(1, length):
            if nums_[i] == (nums_[i-1] + 1):
                curr += 1
            else:
                curr = 1

            dp[i] = max(curr, dp[i-1])
        
        return dp[-1]

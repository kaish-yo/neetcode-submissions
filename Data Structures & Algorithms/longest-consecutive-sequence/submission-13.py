class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_ = sorted(set(nums))

        if len(nums_) == 0:
            return 0

        dp = [1] * len(nums_)
        
        curr = 1
        for i in range(1, len(nums_)):
            if nums_[i] == nums_[i - 1] + 1:
                curr += 1
            else:
                curr = 1
            
            dp[i] = max(dp[i - 1], curr)
        
        return dp[-1]            


        
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        dp = []
        dp = [0] * len(nums)

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        n = 2

        while n < len(nums):
            if dp[n - 2] + nums[n] > dp[n - 1]:
                dp[n] = dp[n - 2] + nums[n]
            else:
                dp[n] = dp[n - 1]
            
            n += 1
        
        return dp[-1]
            

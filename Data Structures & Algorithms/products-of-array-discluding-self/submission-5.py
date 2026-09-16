class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        results = [1] * length
        
        # prefix
        prefix = 1
        for i in range(0, length):
            results[i] *= prefix
            prefix *= nums[i]
        
        # suffix
        suffix = 1
        for i in range(length - 1, -1, -1):
            results[i] *= suffix
            suffix *= nums[i]
        
        return results

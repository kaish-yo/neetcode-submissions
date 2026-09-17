class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        res = [1] * length

        # prefix
        prefix = 1
        for i in range(0, length):
            res[i] *= prefix
            prefix *= nums[i]
        
        # suffix
        suffix = 1
        for i in range(length - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res


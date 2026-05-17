class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            bs_idx = (left + right) // 2

            if target < nums[bs_idx]:
                right = bs_idx - 1
            elif target > nums[bs_idx]:
                left = bs_idx + 1
            elif target == nums[bs_idx]:
                return bs_idx
        
        return -1
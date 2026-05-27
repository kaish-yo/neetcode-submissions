class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) >= k:
            nums.sort()
            return nums[-k]
        else:
            return
        
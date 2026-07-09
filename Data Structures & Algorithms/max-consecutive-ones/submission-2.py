class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        count = 0
        
        for num in nums:
            if num:
                count += 1
                best = max(count, best)
            else:
                count = 0
        
        return best
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        end = 0
        lens = [0]

        while end < len(nums):
            count = 0
            for i in range(end, len(nums)):
                if nums[i] == 1:
                    count += 1
                    if i == len(nums) - 1:
                        lens.append(count)
                        end = len(nums)
                    continue
                
                lens.append(count)
                end = i + 1
                break
        
        return max(lens)
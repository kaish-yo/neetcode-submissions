class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = dict()

        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        for c in count_map.values():
            if c > 1:
                return True
        
        return False

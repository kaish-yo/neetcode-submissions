class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appeared = set()


        for n in nums:
            if n in appeared:
                return n
            
            appeared.add(n)
        
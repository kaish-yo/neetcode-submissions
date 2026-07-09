class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_arr = [num for num in nums if num != val]
        nums[:len(new_arr)] = new_arr
        return len(new_arr)
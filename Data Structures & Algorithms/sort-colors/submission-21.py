class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket_list = [0] * 3

        for num in nums:
            bucket_list[num] += 1
        
        pointer = 0

        for color in range(len(bucket_list)):
            for count in range(bucket_list[color]):
                nums[pointer] = color
                pointer += 1
        
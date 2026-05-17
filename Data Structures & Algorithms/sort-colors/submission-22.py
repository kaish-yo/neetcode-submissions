class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket_list = [0 for _ in range(3)]

        for i in nums:
            bucket_list[i] += 1
        
        pointer = 0

        for color in range(len(bucket_list)):
            for count in range(bucket_list[color]):
                nums[pointer] = color
                pointer += 1
        
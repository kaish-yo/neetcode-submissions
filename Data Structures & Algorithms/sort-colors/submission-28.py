class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]

        for num in nums:
            bucket[num] += 1
        
        pointer = 0
        
        i = 0
        for n in range(len(bucket)):
            for _ in range(bucket[n]):
                nums[i] = n
                i += 1
        
        # res = []

        # for idx, count in enumerate(bucket):
        #     for _ in range(count):
        #         res.append(idx)
        
        
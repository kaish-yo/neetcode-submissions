class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict()

        for num in nums:
            if not num in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        nums_sorted = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)

        nums_sorted = [num[0] for num in nums_sorted]
        
        return nums_sorted[:k]

    

            

       


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res_ = {
            num: 0
            for num in set(nums)
        }

        for num in nums:
            res_[num] += 1

        res_ = list(res_.items())
        res_.sort(key=lambda x: x[1], reverse=True)
        res = [i[0] for i in res_]

        return res[:k]


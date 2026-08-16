from _heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        
        res = 0
        for _ in range(k):
            res = heapq.heappop(heap)
        
        return -res
        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [ (p[0]**2 + p[1]**2, p[0], p[1]) for p in points]
        heapq.heapify(min_heap)
        
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append([x, y])

        return res
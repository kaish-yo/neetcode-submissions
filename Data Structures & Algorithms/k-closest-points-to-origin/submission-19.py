class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_ = [(math.sqrt(p[0]**2 + p[1]**2), p) for p in points]
        points_.sort()
        return [p[1] for p in points_][:k]
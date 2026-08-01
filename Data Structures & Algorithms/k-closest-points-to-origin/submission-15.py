import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [math.sqrt(point[0]**2 + point[1]**2) for point in points]
        dist_to_point = [
            (dists[idx], points[idx])
            for idx, _ in enumerate(points)
        ]
        dist_to_point = sorted(dist_to_point)
        print(dist_to_point)

        res = [item[1] for item in dist_to_point]
        
        return res[:k]
        
        
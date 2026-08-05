class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            time_ = 0   

            for pile in piles:
                time_ += (pile + mid - 1) // mid
            
            if time_ <= h:
                hi = mid
            else: 
                lo = mid + 1

        return lo
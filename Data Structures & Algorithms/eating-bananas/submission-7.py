class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo = 1
        hi = max(piles)

        while lo < hi:

            mid = (lo + hi) // 2
            estimate = 0

            for pile in piles:
                time_ = (pile + mid - 1) // mid
                estimate += time_

            if estimate <= h:
                hi = mid
            else:
                lo = mid + 1

        return lo
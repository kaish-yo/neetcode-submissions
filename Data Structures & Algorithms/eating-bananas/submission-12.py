class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lo, hi = 1, max(piles)

        while lo < hi:
            unit = (hi + lo) // 2
            time_ = 0

            for pile in piles:
                time_ += (pile + unit - 1) // unit

            if time_ <= h:
                hi = unit
            else:
                lo = unit + 1 #　切り捨てされちゃうから切り上げる
        
        return lo
            



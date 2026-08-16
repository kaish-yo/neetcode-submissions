import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_ = [-s for s in stones] # Max heapinize
        heapq.heapify(stones_)

        while len(stones_) > 1:
            x = heapq.heappop(stones_)
            y = heapq.heappop(stones_)

            if x < y:
                heapq.heappush(stones_, x - y)
        
        if stones_:
            return abs(heapq.heappop(stones_))
        
        return 0


                
        


        
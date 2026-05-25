class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop() # remove the heaviest
                stones.pop() # remove the second heaviest
            
            else:
                first = stones.pop()
                second = stones.pop()
                new = first - second
                stones.append(new)
                stones.sort()
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

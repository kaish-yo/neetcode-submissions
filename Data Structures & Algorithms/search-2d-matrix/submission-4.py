class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        for row in matrix:
            flattened.extend(row)
        
        left, right = 0, len(flattened) - 1

        while left <= right:
            bs_index = (right + left) // 2

            if target < flattened[bs_index]:
                right = bs_index - 1
            elif target > flattened[bs_index]:
                left = bs_index + 1
            else:
                return True
        
        return False
            


        # if target in flattened:
        #     return True
        # else:
        #     return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = []
        for row in matrix:
            flattened.extend(row)

        if target in flattened:
            return True
        else:
            return False
        
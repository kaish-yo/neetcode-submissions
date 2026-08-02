class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            for col in row:
                arr.append(col)
        
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2

            if target < arr[mid]:
                R = mid - 1
            elif arr[mid] < target:
                L = mid + 1
            else:
                return True
        
        return False
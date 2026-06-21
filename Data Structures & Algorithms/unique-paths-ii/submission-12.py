class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid = [[-c for c in row] for row in obstacleGrid]

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * COLS for _ in range(ROWS)]
        
        def count_paths(r, c, cache):
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            if r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == -1:
                return 0
            if cache[r][c] != 0:
                return cache[r][c]
            
            cache[r][c] = count_paths(r + 1, c, cache) + count_paths(r, c + 1, cache)
            return cache[r][c]
        
        return count_paths(0, 0, cache)
        
    

        
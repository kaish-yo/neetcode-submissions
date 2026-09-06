class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        if ROWS == 1 and COLS == 1:
            return 1

        prev_row = [0] * COLS
        prev_row[-1] = 1

        i = ROWS - 1

        while i >= 0:
            curr_row = [0] * COLS

            for col in range(COLS - 1, -1, -1):
                if obstacleGrid[i][col] == 1:
                    continue
                if col == COLS - 1:
                    curr_row[col] = prev_row[col]
                else:
                    curr_row[col] = curr_row[col + 1] + prev_row[col]
            
            prev_row = curr_row
            i -= 1
        
        return prev_row[0]
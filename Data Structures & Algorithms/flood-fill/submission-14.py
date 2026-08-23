class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        target_color = image[sr][sc]
        visited = set()

        def dfs(row, col):
            if (min(row, col) < 0 or
                (row>=ROWS) or
                (col>=COLS) or
                (row, col) in visited or
                (image[row][col] != target_color)):

                return
            visited.add((row, col))
            
            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image
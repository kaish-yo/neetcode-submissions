class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= rows or c >= cols or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0
            
            size = 1
            
            size += dfs(r + 1, c)
            size += dfs(r - 1, c)
            size += dfs(r, c + 1)
            size += dfs(r, c - 1)

            return size

        sizes = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    sizes.append(dfs(r, c))
        
        if sizes:
            return max(sizes)
        else:
            return 0
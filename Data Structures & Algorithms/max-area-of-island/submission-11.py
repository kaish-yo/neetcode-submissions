class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if (
                min(r, c) < 0 or
                r >= ROWS or c >= COLS or
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
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]: 
                    sizes.append(dfs(r, c))
        
        if sizes:
            return max(sizes)
        else:
            return 0

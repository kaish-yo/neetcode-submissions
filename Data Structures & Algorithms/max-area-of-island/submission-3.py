class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sizes = []

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            # 範囲外、または水(または訪問済み)なら終了
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0

            # 訪問済みにする（0 に塗りつぶす）
            grid[r][c] = 0
            size = 1

            # 上下左右へ探索
            size += dfs(r + 1, c)
            size += dfs(r - 1, c)
            size += dfs(r, c + 1)
            size += dfs(r, c - 1)
            
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    sizes.append(size)      # その島を丸ごと潰す

        if sizes:
            return max(sizes)
        else:
            return 0
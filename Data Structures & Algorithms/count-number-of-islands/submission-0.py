class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> None:
            # 範囲外、または水(または訪問済み)なら終了
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"):
                return

            # 訪問済みにする（"0" に塗りつぶす）
            grid[r][c] = "0"

            # 上下左右へ探索
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1   # 新しい島を発見
                    dfs(r, c)      # その島を丸ごと潰す

        return islands
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRECTIONS:
                    tr, tc = r + dr, c + dc
                    if 0 <= tr < ROWS and 0 <= tc < COLS and grid[tr][tc] == 1:
                        grid[tr][tc] = 2
                        fresh -= 1
                        q.append((tr, tc))
            minutes += 1

        return minutes if fresh == 0 else -1
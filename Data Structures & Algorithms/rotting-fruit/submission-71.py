class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not any(1 in row for row in grid):
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    q.append((r, c))

        neighbours = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        minutes = 0
        while q:
            if not any(1 in row for row in grid):
                return minutes

            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbours:
                    tr, tc = r + dr, c + dc

                    if (
                        min(tr, tc) < 0 or
                        tr >= ROWS or
                        tc >= COLS or
                        grid[tr][tc] != 1
                    ):
                        continue
                    
                    grid[tr][tc] = 2
                    q.append((tr, tc))

            minutes += 1
        
        return minutes if not any(1 in row for row in grid) else -1
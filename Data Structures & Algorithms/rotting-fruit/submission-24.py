class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        f_grid = [c for r in grid for c in r]
        grid_ = [row[:] for row in grid]
        
        if 1 not in f_grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        minutes = 0
        ds = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in ds:
                    tr, tc = r + dr, c + dc

                    if (
                        tr < 0 or tc < 0 or
                        tr >= ROWS or tc >= COLS or
                        grid_[tr][tc] == 0 or
                        grid_[tr][tc] == 2
                    ):  

                        continue
                    
                    grid_[tr][tc] = 2
                    q.append((tr, tc))
            if q:
                minutes += 1
        
        f_grid_ = [c for r in grid_ for c in r]

        if 1 in f_grid_:
            return -1
        
        return minutes
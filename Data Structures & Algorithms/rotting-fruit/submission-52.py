class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        f_grid = [i for r in grid for i in r]
        minutes = 0

        if not 2 in f_grid and not 1 in f_grid:
            return 0
        
        if not 2 in f_grid and 1 in f_grid:
            return -1
        
        ds = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            if not 1 in [i for r in grid for i in r]:
                return minutes

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in ds:
                    tr, tc = r + dr, c + dc
                    
                    if (
                        tr < 0 or tc < 0 or
                        tr >= ROWS or tc >= COLS or
                        grid[tr][tc] == 0 or grid[tr][tc] == 2
                    ):  
                        continue
                    
                    grid[tr][tc] = 2
                    q.append((tr, tc))
            
            minutes += 1
        
        if not 1 in [i for r in grid for i in r]:
            return minutes
        else:
            return -1

                    




    

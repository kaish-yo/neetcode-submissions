class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))

        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS -1 and c == COLS - 1:
                    return length + 1

                neighbors = [
                    (0, 1), 
                    (0, -1),
                    (1, 1),
                    (-1, -1),
                    (1, -1),
                    (-1, 1), 
                    (1, 0), 
                    (-1, 0),
                ]

                for dr, dc in neighbors:
                    rt, ct = (r + dr), (c + dc)
                    if (
                        min(rt, ct) < 0 or
                        rt >= ROWS or ct >= COLS or
                        grid[rt][ct] == 1 or
                        (rt, ct) in visited
                    ):
                        continue

                    q.append((rt, ct))
                    visited.add((rt, ct))
            
            length += 1
        
        return -1
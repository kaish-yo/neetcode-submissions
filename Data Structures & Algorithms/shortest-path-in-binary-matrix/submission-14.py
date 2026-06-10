class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))

        ds = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, 1),
            (1, -1),
            (-1, -1),
        ]
        
        length = 1

        while q:
            for i in range(len(q)):
                r, c =  q.popleft()
                if r == ROWS -1 and c == COLS -1:
                    return length

                for dr, dc in ds:
                    tr, tc = r + dr, c + dc
                    if (
                        tr < 0 or tc < 0 or tr >= ROWS or tc >= COLS or 
                        (tr, tc) in visited or grid[tr][tc] == 1
                    ):
                        continue
                    
                    q.append((tr, tc))
                    visited.add((tr, tc))
                
            length += 1
        
        return -1
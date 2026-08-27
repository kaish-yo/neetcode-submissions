class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        visited = set()

        q.append((0, 0))
        visited.add((0, 0))

        length = 1

        neighbours = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length

                for dr, dc in neighbours:
                    tr, tc = r + dr, c + dc

                    if (
                        min(tr, tc) < 0 or
                        tr >= ROWS or
                        tc >= COLS or
                        grid[tr][tc] != 0 or
                        (tr, tc) in visited                        
                    ):
                        continue
                    
                    q.append((tr, tc))
                    visited.add((tr, tc))
            
            length += 1

        return -1
        




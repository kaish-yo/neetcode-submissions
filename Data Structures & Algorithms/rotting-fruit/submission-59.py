class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0: return 0
        
        mins = -1
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            mins += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in neighbours:
                    tr, tc = r + dr, c + dc
                    if (0 <= tr < ROWS and 0 <= tc < COLS and grid[tr][tc] == 1):
                        grid[tr][tc] = 2
                        fresh -= 1
                        q.append((tr, tc))

        return mins if fresh == 0 else -1
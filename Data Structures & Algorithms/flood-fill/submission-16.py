class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        target_color = image[sr][sc]
        visited = set()

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r >= ROWS or 
                c >= COLS or
                image[r][c] != target_color or
                (r, c) in visited
            ):
                return
            
            image[r][c] = color
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image

            



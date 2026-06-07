class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROW, COL = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        def dfs(r, c):
            if min(r, c) < 0:
                return
            
            if r >= ROW or c >= COL:
                return
            
            if image[r][c] != start_color:
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image
            





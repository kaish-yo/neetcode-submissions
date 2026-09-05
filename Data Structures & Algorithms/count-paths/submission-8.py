class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n
        prev_row[-1] = 1

        for row in range(m - 1, -1, -1):
            print(prev_row)
            curr_row = [0] * n
            curr_row[-1] = 1

            for col in range(n - 2, -1, -1):
                curr_row[col] = prev_row[col] + curr_row[col + 1]
            
            prev_row = curr_row[:]
        
        return prev_row[0]

        
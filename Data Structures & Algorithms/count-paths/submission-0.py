class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0]*n for _ in range(m)]
        paths[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    paths[i][j] = 1
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        
        return paths[-1][-1]
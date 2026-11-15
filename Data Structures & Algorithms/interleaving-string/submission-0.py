class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[False]*(len(s1)+1) for _ in range(len(s2)+1)]
        dp[0][0] = True

        for i in range(len(s2)+1):
            for j in range(len(s1)+1):
                

                if not dp[i][j]:
                    continue
                
                k = i + j

                if i < len(s2) and s2[i] == s3[k]:
                    dp[i + 1][j] = True
                if j < len(s1) and s1[j] == s3[k]:
                    dp[i][j+1] = True

        return dp[len(s2)][len(s1)]
                
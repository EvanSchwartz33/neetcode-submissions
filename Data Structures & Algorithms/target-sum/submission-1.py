class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = 0
        for num in nums:
            s+= abs(num)
        
        if abs(target) > s:
            return 0

        dp = [0]*(s*2+1)
        dp[s] = 1
        for num in nums:
            next_dp = [0]*len(dp)

            for i, count in enumerate(dp):
                if count:
                    next_dp[i + num] += count
                    next_dp[i - num] += count

            dp = next_dp
        
        return dp[target + s]


        

        
        
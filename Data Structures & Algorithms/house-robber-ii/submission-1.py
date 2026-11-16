class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))

        if len(nums) == 1:
            return nums[-1]

        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2,len(dp)):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        best = dp[-1]

        dp[0] = 0
        dp[1] = nums[1]

        for i in range(2,len(dp)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        if dp[-1] > best:
            best = dp[-1]
        


        return best
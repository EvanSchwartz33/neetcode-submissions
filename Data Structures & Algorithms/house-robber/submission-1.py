class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [0]*(len(nums) + 1)
        arr[0] = 0
        arr[1] = nums[0] if len(nums) > 0 else 0
        for i in range(1,len(nums)):
            arr[i+1] = max(arr[i-1]+nums[i],arr[i])

        return arr[-1] 
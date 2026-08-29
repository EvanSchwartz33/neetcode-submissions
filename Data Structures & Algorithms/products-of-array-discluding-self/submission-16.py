class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answers = [1] * len(nums)
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)
        for i in range (1,len(nums)):
                prefixes [i] = prefixes[i-1] * nums[i-1]
                answers[i] = prefixes[i]
        for i in range (len(nums) - 2, -1, -1):
                postfixes[i] = postfixes[i+1] * nums[i+1]
                answers[i] *= postfixes[i]
        return answers
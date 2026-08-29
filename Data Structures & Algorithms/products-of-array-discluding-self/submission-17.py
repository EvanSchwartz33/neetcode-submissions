class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answers = [1] * len(nums)
        prefix = 1
        postfix = 1
        for i in range (1,len(nums)):
                prefix = prefix * nums[i-1]
                answers[i] = prefix
        for i in range (len(nums) - 2, -1, -1):
                postfix = postfix * nums[i+1]
                answers[i] *= postfix
        return answers
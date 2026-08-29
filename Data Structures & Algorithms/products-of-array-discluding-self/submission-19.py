class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)
        prefix = 1
        
        for i in range (len(nums)):
                answers[i] = prefix
                prefix = prefix * nums[i]
                
        postfix = 1
        for i in range (len(nums) - 1, -1, -1):
                answers[i] *= postfix
                postfix = postfix * nums[i]
                
        return answers
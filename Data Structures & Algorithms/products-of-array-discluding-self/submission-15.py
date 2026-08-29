class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        answers = [1] * len(nums)
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)
        for i in range (1,len(nums)):
                prefixes [i] = prefixes[i-1] * nums[i-1]
        for i in range (len(nums) - 2, -1, -1):
                postfixes[i] = postfixes[i+1] * nums[i+1]
        for i in range (0,len(nums)):
            answers[i] = prefixes[i] * postfixes[i] 
        return answers
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            k = (left + right)//2

            if nums[k] <= nums[right]:
                right = k
            else:
                left = k + 1
        
        return nums[left]


        
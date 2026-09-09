class Solution:
    def search(self, nums: List[int], target: int) -> int:
       left = 0
       right = len(nums)-1

       while left <= right:
            k = (right + left)//2
            if nums[k] == target:
                return k
            if nums[k] < target:
                left = k+1
            else:
                right = k-1
        
       return -1

       
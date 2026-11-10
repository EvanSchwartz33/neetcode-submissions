class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            k = (left + right)//2

            if nums[k] == target:
                return k
            elif nums[right] > nums[k]:
                if target > nums[k] and target <= nums[right]:
                    left = k + 1
                else:
                    right = k - 1
            else:
                if target < nums[k] and target >= nums[left]:
                    right = k - 1
                else:
                    left = k + 1

        
        return -1

            
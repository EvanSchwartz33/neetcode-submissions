class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        i = 0
        while i < len(nums):
            if i > 0:
                while nums[i] == nums[i-1]:
                    i += 1
                    if i == len(nums):
                        return answer
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    array = [nums[i], nums[left],nums[right]]
                    
                    answer.append(array)

                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    continue
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
            i += 1
        return answer

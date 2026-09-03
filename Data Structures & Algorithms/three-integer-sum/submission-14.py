class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range (0,len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    array = [nums[i], nums[left],nums[right]]
                    array.sort()
                    if array not in answer:
                        answer.append(array)
                    left += 1
                    continue
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return answer

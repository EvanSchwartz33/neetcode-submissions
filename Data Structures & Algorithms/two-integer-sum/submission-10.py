class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range (len(nums)):
            x = nums[i]
            y = target - nums[i]
            
            if(y in hashmap):
                return [hashmap[y],i]

            hashmap[x] = i

        return []

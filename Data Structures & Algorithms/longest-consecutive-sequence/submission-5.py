class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = []
        nums = set(nums)
        for num in nums:
            tempset = []
            pointer = num
            if num - 1 in nums:
                continue
            if num in answer:
                continue

            tempset.append(num)
            while pointer + 1 in nums:
                tempset.append(pointer + 1)
                pointer += 1
            
            if len(tempset) > len(answer):
                answer = tempset
            
        return len(answer)
            
            
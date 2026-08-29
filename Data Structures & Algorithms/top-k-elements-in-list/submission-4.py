class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            
            hashmap[num] = hashmap[num] + 1
        answer = []
        i = 0
        while i < k:
            maxnum = max(hashmap.values())
            for key,val in hashmap.items():
                if val == maxnum:
                    answer.append(key)
                    hashmap[key] = 0
                    i += 1


        return answer
        
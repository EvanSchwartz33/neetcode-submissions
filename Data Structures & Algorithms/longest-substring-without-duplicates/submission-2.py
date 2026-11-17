class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start = 0
        best = 0

        for i, char in enumerate(s):
            if char in hashmap:
                if hashmap[char] >= start:
                    start = hashmap[char] + 1
                    hashmap[char] = i
                else:
                    hashmap[char] = i
            else:
                hashmap[char] = i
            
            if (i - start + 1) > best:
                best = i - start + 1
        
        return best

            
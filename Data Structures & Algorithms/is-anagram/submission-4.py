class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        hashmap = {}
        for char in s:
            x = 0
            if char in hashmap:
                x =hashmap.get(char)
            
            x += 1
            hashmap[char] = x

        for char in t:
            if char not in hashmap:
                return False
            
            x = hashmap.get(char)
            x -= 1
            if (x < 0):
                return False

            hashmap[char] = x

        return True
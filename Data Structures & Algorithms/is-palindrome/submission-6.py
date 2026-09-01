class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for char in s:
            if char.isalnum():
                clean = clean + char.lower()
        front = 0
        last = len(clean) - 1
        while front < last:
            if(clean[front] != clean[last]):
                return False
            
            front += 1
            last -= 1
        return True
    
    
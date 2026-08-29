class Solution:

    def encode(self, strs: List[str]) -> str:
        answer1 = ""
        for word in strs:
            answer1 += str(len(word)) + "/" + word

        return answer1
    def decode(self, s: str) -> List[str]:
        answer2 = []
        word = ""
        i = 0
        while i < len(s):
            j = i
            while s[j] != "/":
                j += 1
            
            length = int(s[i:j])
            
            word = s[j+1:j+1+length]
            answer2.append(word)
            i = j + 1 + length
            
        return answer2  


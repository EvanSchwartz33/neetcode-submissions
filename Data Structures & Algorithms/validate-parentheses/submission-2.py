class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range (0,len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if s[i] == ')':
                    if stack:
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                if s[i] == ']':
                    if stack:
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
                if s[i] == '}':
                    if stack:
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                    else:
                        return False
        if stack:
            return False
        else:
            return True
        


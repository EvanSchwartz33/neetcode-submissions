class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for cur in tokens:
            if cur in ["+","-","/","*"]:
                right = stack.pop()
                left = stack.pop()
                
                if cur == "+":
                    result = left + right
                if cur == "-":
                    result = left - right
                if cur == "*":
                    result = left * right
                if cur == "/":
                    result = int(left / right)
                stack.append(result)
            else:
                stack.append(int(cur))
                
        return stack[-1]

            
        
        
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = [0]*len(temperatures)
        for i in range (0, len(temperatures)):
            if stack:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    index = stack.pop()
                    answers[index] = i - index
            stack.append(i)

        return answers 


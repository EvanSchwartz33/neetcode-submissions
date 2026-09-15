class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        cur_max = 0
        stack.append((heights[0],0))
        for i in range (1,len(heights)):
            if heights[i] > stack[-1][0]:
                stack.append((heights[i],i))
            elif(heights[i] < stack[-1][0]):
                while stack and heights[i] < stack[-1][0]:
                    temp = stack.pop()
                    area = temp[0] * (i-temp[1])
                    if area > cur_max:
                        cur_max = area
                stack.append((heights[i],temp[1]))
        while stack:
            temp = stack.pop()
            area = temp[0] * (len(heights)-temp[1])
            if area > cur_max:
                cur_max = area



        return int(cur_max)
            
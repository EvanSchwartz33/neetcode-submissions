class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1 or len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        max_left = height[0]
        max_right = height[len(height) - 1]
        water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                if height[left] < max_left:
                    water += max_left - height[left] 
                else:
                    max_left = height[left]
            else:
                right -= 1
                if height[right] < max_right:
                    water += max_right - height[right]
                else:
                    max_right = height[right]

        return water


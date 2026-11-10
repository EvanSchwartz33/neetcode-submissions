import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        left = 1
        right = piles[len(piles)-1]
        best_k = float('inf')
        while left <= right:
            hours = 0

            k = (left + right)//2

            for pile in piles:
                hours += math.ceil(pile/k)
                       
            if hours > h:
                left = k + 1
            else:
                if k < best_k:
                    best_k = k
                right = k - 1
            
                
                
        
        return best_k
        

        
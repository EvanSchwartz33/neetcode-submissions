class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0]*(len(cost) + 1)

        arr[0] = cost[0]
        arr[1] = cost[1]

        for i in range(2,len(arr)):
            arr[i] = min(arr[i-2],arr[i-1]) + (cost[i] if i < len(cost) else 0)

        return arr[-1]
        

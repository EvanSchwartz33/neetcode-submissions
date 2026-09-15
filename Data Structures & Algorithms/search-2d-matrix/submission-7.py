class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            k = (left + right)//2
            if matrix[k][0] <= target:
                if k+1 >= len(matrix) or (matrix[k+1][0] > target):
                    new_left = 0
                    new_right = len(matrix[k]) - 1
                    while new_left <= new_right:
                        new_k = (new_left + new_right)//2
                        if matrix[k][new_k] == target:
                            return True
                        elif matrix[k][new_k] < target:
                            new_left = new_k + 1
                        else:
                            new_right = new_k - 1
                    return False
                else:
                    left = k + 1
            elif matrix[k][0] > target:
                right = k - 1
        return False

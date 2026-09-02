class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for row in range(len(matrix)):
        #     l, r = 0, len(matrix[row])-1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if matrix[row][mid] == target:
        #             return True
        #         elif matrix[row][mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1  
        # return False    

        row, col = len(matrix), len(matrix[0])
        l, r = 0, row*col - 1

        while l <= r:
            mid = (l+r)//2
            row, cols = mid // col, mid % col
            if matrix[row][cols] == target:
                return True
            elif matrix[row][cols] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False                          

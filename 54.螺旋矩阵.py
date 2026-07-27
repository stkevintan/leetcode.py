#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        ans = []
        while top <= bottom and left <= right:
            if top == bottom:
                for col in range(left, right + 1):
                    ans.append(matrix[top][col])
                break
            if left == right:
                for row in range(top, bottom + 1):
                    ans.append(matrix[row][left])
                break
            for col in range(left, right):
                ans.append(matrix[top][col])
            for row in range(top, bottom):
                ans.append(matrix[row][right])
            for col in range(right, left, -1):
                ans.append(matrix[bottom][col])
            for row in range(bottom, top, -1):
                ans.append(matrix[row][left])
    
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return ans
        
# @lc code=end


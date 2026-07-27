#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m
        while left < right:
            mid = (left + right) >> 1
            val = matrix[mid // m][mid % m]
            if val == target:
                return True
            if val < target:
                left = mid + 1
            else:
                right = mid
        return False
 
# @lc code=end


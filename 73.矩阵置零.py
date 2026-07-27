#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0 - no, 1 - row, 2 - col, 3 - cross
        corner_mark = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0:
                    continue
                if i == 0:
                    corner_mark |= 1
                if j == 0:
                    corner_mark |= 2
                matrix[0][j] = 0
                matrix[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if corner_mark & 1:
            for j in range(0, m):
                matrix[0][j] = 0

        if corner_mark & 2:
            for i in range(0, n):
                matrix[i][0] = 0
        
# @lc code=end


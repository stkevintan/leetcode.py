#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        end = n - 1
        start = 0
        while end - start > 0:
            for i in range(start, end):
                tmp = matrix[i][start]
                print("1. %d,%d" % (i, start))
                matrix[i][start] = matrix[end][i]
                print("2. %d,%d" % (end, i))
                matrix[end][i] = matrix[n - i - 1][end]
                matrix[n - i - 1][end] = matrix[start][n-i - 1]
                matrix[start][n -1 -i] = tmp
            end -= 1
            start += 1
        
# @lc code=end


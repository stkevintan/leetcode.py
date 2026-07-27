#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        p = [m - 1, 0]
        while matrix[p[0]][p[1]] != target:
            if matrix[p[0]][p[1]] > target:
                p[0] -= 1
                if p[0] < 0: return False
            else:
                p[1] += 1
                if p[1] >= n: return False
        return True

# @lc code=end


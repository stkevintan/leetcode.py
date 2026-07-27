#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
import math
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [-1] * m
        dp[0] = 0
        for row in range(n):
            for col in range(m):
                if col == 0:
                    dp[0] += grid[row][0]
                    continue
                candidates =[c for c in (dp[col], dp[col - 1]) if c != -1] 
                dp[col] = min(candidates, default=0) + grid[row][col]
        return dp[-1]
# @lc code=end


#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(x, y):
            if grid[x][y] == '-1' or grid[x][y] == '0':
                return
            grid[x][y] = '-1'
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    dfs(nx, ny)
        ans = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    ans += 1
                    dfs(i, j)
        return ans
        
# @lc code=end


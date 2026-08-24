#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def bfs(x: int, y: int)-> int:
            sum = 0
            q = deque[tuple[int, int]]([(x, y)])
            grid[x][y] = 0
            while q:
                (x, y) = q.popleft()
                sum += 1
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        q.append((nx, ny))
            return sum

        def find():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        yield bfs(i, j)
        return max(find(), default=0)
        
                    
# @lc code=end


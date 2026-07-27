#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n,m  = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        time = 0
        while len(q):
            (i, j, t) = q.popleft()
            time = max(time, t)
            for ni, nj in ((i-1, j), (i, j -1), (i +1, j), (i, j+1)):
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni, nj, t + 1))

        if any(1 in row for row in grid):
            return -1
        return time
                    


# @lc code=end


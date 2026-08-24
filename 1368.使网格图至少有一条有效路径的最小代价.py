#
# @lc app=leetcode.cn id=1368 lang=python3
#
# [1368] 使网格图至少有一条有效路径的最小代价
#

# @lc code=start
from collections import deque


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        INF = 10 **9
        n, m = len(grid), len(grid[0])
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0
        Q = deque([(0, 0)])
        while Q:
            (x, y) = Q.popleft()
            if x == n - 1 and y == m - 1: return dist[x][y]
            for dx, dy, dir in [(1, 0, 3), (-1, 0, 4), (0, 1, 1), (0, -1, 2)]:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m:
                    w = 0 if dir == grid[x][y] else 1
                    if dist[x][y] + w < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + w
                        # 0 - 1 BFS
                        if w == 0: Q.appendleft((nx, ny))
                        else: Q.append((nx, ny))
        return 0
        
# @lc code=end


#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] 网格中的最短路径
#

# @lc code=start
from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[[-1] * (k + 1) for _ in range(m)] for _ in range(n)]
        # i, j, k
        dist[0][0][k] = 0
        Q = deque[tuple[int, int, int]]()
        Q.append((0, 0, k))
        while Q:
            (i, j, left)= Q.popleft()
            if i == n - 1 and j == m - 1:
                return dist[i][j][left]
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + dx, j + dy
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                # if grid[x][y] is wall, left should minus 1
                l = left - grid[x][y]
                if l < 0:
                    continue
                if dist[x][y][l] == -1:
                    dist[x][y][l] = dist[i][j][left] + 1
                    Q.append((x, y, l))
        return -1



        
# @lc code=end


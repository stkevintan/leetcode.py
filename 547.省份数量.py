#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            parent[ra] = rb

        for i, edge in enumerate(isConnected):
            for j, ok in enumerate(edge):
                if ok:
                    union(i, j)

        return sum(1 for i in range(n) if find(i) == i)


# @lc code=end


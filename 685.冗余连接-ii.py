#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#

# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)

        def find(parent: list[int], x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # 路径减半
                x = parent[x]
            return x

        def is_tree(skip: int) -> bool:
            """跳过第 skip 条边后，其余 n-1 条边无环即是一棵树"""
            parent = list(range(n + 1))
            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue
                ru, rv = find(parent, u), find(parent, v)
                if ru == rv:
                    return False
                parent[ru] = rv
            return True

        # 情况一：存在入度为 2 的节点 → 答案是指向它的两条边之一
        indeg = [0] * (n + 1)
        for u, v in edges:
            indeg[v] += 1
        cand = [i for i, (u, v) in enumerate(edges) if indeg[v] == 2]
        if cand:
            i2, i1 = cand[1], cand[0]  # 后出现的边优先试删
            return edges[i2] if is_tree(i2) else edges[i1]

        # 情况二：无入度为 2 → 图中唯一环，第一条成环边即答案
        parent = list(range(n + 1))
        for u, v in edges:
            ru, rv = find(parent, u), find(parent, v)
            if ru == rv:
                return [u, v]
            parent[ru] = rv

# @lc code=end


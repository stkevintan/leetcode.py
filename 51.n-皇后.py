#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans: List[List[str]] = []
        queens: List[int] = []                # 只存列号，索引 = 行号
        col_set: set[int] = set()
        diag_set: set[int] = set()            # col - row
        ndiag_set: set[int] = set()           # col + row

        def check(row: int, col: int) -> bool:
            return (col not in col_set and
                    (col - row) not in diag_set and
                    (col + row) not in ndiag_set)

        def place(row: int, col: int):
            queens.append(col)
            col_set.add(col)
            diag_set.add(col - row)
            ndiag_set.add(col + row)

        def remove():
            col = queens.pop()
            row = len(queens)                 # 移除后 len = 当前行号
            col_set.remove(col)
            diag_set.remove(col - row)
            ndiag_set.remove(col + row)

        def as_board() -> List[str]:
            return ['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens]

        def dfs(row: int):
            if row == n:
                ans.append(as_board())
                return
            for col in range(n):
                if check(row, col):
                    place(row, col)
                    dfs(row + 1)
                    remove()

        # 对称性剪枝：第一行只搜前一半列，镜像补齐
        mid = (n + 1) // 2
        for col in range(mid):
            place(0, col)
            before = len(ans)
            dfs(1)
            for board in ans[before:]:
                mirrored = [r[::-1] for r in board]
                if n % 2 == 0 or col != n // 2:
                    ans.append(mirrored)
                # 奇数 n 的中间列：镜像仍在中间列，DFS 已找到全部，不加
            remove()

        return ans


# @lc code=end


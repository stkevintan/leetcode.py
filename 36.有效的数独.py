#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n, m = len(board), len(board[0])
        rows, cols, grids = [0] * n, [0] * m, [[0] * (m // 3) for _ in range(n // 3)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                mask = 1 << (int(board[i][j]) - 1)
                if rows[i] & mask or cols[j] & mask or grids[i // 3][j // 3] & mask:
                    return False
                rows[i] |= mask
                cols[j] |= mask
                grids[i // 3][j // 3] |= mask
        return True

# @lc code=end


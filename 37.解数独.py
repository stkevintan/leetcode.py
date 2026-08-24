#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def ch2mask(self, ch: str):
        return 1 << (int(ch) - 1)
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1-9 映射到 0-8
        n, m = len(board), len(board[0])
        FULL = (1 << 9) - 1  # 位 0..8 全置 1
        rows, cols, grids = [0] * n, [0] * m, [[0] * 3 for _ in range(3)]


        for i in range(n):
            for j in range(m):
                if board[i][j] != '.':
                    mask = self.ch2mask(board[i][j])
                    rows[i] |= mask
                    cols[j] |= mask
                    grids[i // 3][j // 3] |= mask

        def dfs() -> bool:
            # MRV：选候选数最少的空格
            best: tuple[int, int] | None = None
            best_cand = 0
            for i in range(n):
                for j in range(m):
                    if board[i][j] == '.':
                        cand = FULL & ~(rows[i] | cols[j] | grids[i // 3][j // 3])
                        if cand == 0:
                            return False  # 某格无候选，提前剪枝
                        if best is None or cand.bit_count() < best_cand.bit_count():
                            best, best_cand = (i, j), cand
            if best is None:
                return True
            x, y = best
            cand = best_cand
            while cand:
                bit = cand & -cand  # 取最低位候选
                cand ^= bit
                board[x][y] = str(bit.bit_length())
                rows[x] |= bit
                cols[y] |= bit
                grids[x // 3][y // 3] |= bit
                if dfs():
                    return True
                board[x][y] = '.'
                rows[x] ^= bit
                cols[y] ^= bit
                grids[x // 3][y // 3] ^= bit
            return False

        dfs()



        
# @lc code=end


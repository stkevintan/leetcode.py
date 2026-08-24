#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#

# @lc code=start
class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        n = len(grid)
        NEG = -10 ** 9
        # r1 c1: 第一个人走了多少行， 多少列
        # dp[r1][r2]: 两人同步走了 t 步（r+c = t）时的最大樱桃数
        dp = [[[NEG] * n for _ in range(n)] for _ in range(2)]
        dp[0][0][0] = grid[0][0]
        for t in range(1, 2 * n - 1):
            cur, prev = t % 2, (t - 1) % 2
            for r1 in range(n):  # 重置当前槽：跳过格不能残留 t-2 层的值
                for r2 in range(n):
                    dp[cur][r1][r2] = NEG
            for r1 in range(n):
                for r2 in range(n):
                    c1, c2 = t - r1, t - r2
                    if not (0 <= c1 < n and 0 <= c2 < n):
                        continue
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    best = max(dp[prev][pr1][pr2]
                               for pr1 in (r1 - 1, r1)
                               for pr2 in (r2 - 1, r2)
                               if 0 <= pr1 < n and 0 <= pr2 < n)
                    if best != NEG:
                        # 同格（r1 == r2 ⟺ c1 == c2）樱桃只计一次
                        gain = grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0)
                        dp[cur][r1][r2] = best + gain
        return max(dp[(2 * n - 2) % 2][n - 1][n - 1], 0)

# @lc code=end


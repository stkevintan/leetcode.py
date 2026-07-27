#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [100000] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                dp[i] = min(dp[i], dp[i - k * k] + 1)
                k += 1
        return dp[n]
# @lc code=end


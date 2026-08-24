#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 1
        for k in range(2, n + 1):        # 分成 k 份，k 最大为 n
            m, r = divmod(n, k)          # 每份尽量均分：r 份 m+1，k-r 份 m
            mul = (m + 1) ** r * m ** (k - r)
            ans = max(ans, mul)
        return ans
# @lc code=end


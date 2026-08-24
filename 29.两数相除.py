#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sig1 = 1 if dividend >= 0  else -1
        sig2 = 1 if divisor >= 0 else -1
        sig = sig1 * sig2
        dividend = -abs(dividend)
        divisor = -abs(divisor)

        while dividend <= divisor:
            d2 = divisor
            acc = 1
            while dividend <= d2 + d2:
                d2 = d2 + d2
                acc = acc + acc
            ans -= acc
            dividend -= d2
        if sig > 0 and ans == -2 ** 31:
            return -(ans + 1)

        return -sig * ans
        

# @lc code=end


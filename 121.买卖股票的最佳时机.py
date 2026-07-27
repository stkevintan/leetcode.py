#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices = prices[::-1]
        right = prices[0]
        ans = 0
        for p in prices[1:]:
            ans = max(ans, right - p)
            right = max(right, p)
        return ans
# @lc code=end


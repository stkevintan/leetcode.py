#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(b - a, 0) for a, b in zip(prices, prices[1:]))
# @lc code=end


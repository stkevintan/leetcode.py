#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        first = second = 0
        cur = 0
        for i in range(2, n + 1):
            cur = min(second + cost[i - 1], first + cost[i - 2])
            first = second
            second = cur
        return cur
        
# @lc code=end


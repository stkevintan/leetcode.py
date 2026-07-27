#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List

# [3,3,6,8,16,16,16,18,20]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if 1 & sum(nums):
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                if dp[j - nums[i]]:
                    dp[j] = True

        return dp[target]

# @lc code=end


#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        sum = nums[0]
        for d in nums[1:]:
            sum = max(sum + d, d)
            ans = max(sum ,ans)
        return ans

# @lc code=end


#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除了自身以外数组的乘积
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        for i in range(1, len(ans) - 1):
            ans[i] *= ans[i - 1]
        right = 1
        for i in range(len(ans) - 1, -1, -1):
            left = 1 if i == 0 else ans[i - 1]
            ans[i] = left * right
            right *= nums[i]
        return ans
        
# @lc code=end


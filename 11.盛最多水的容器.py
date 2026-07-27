#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            h = min(height[left], height[right])
            ans = max(ans, h * (right - left))
            # 移动较矮的那一侧
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
# @lc code=end


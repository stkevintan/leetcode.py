#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = deque[int]()
        heights.append(0)
        for i, h in enumerate(heights):
            # 弹出的时候算面积
            while stack and heights[stack[-1]] >  h:
                j = stack.pop()
                left = stack[-1] if stack else -1
                ans = max(ans, heights[j] * (i - left - 1))
            stack.append(i)
        return ans
        
# @lc code=end


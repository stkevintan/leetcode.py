#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def trap2(self, height: List[int]) -> int:
        stack = deque()
        ans = 0
        for (i, v) in enumerate(height):
            base = 0
            while stack and height[stack[-1]] <= v:
                p = stack.pop()
                ans += (i - p - 1) * (height[p] - base)
                base = height[p]
            if stack:
                ans += (v - base) * (i - stack[-1] - 1)
            stack.append(i)
        return ans
    def trap3(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()           # 凹槽底
                if not stack:
                    break                      # 没有左墙，接不住水
                left = stack[-1]               # 左墙
                w = i - left - 1               # 宽度
                hh = min(height[left], h) - height[bottom]  # 水深
                ans += w * hh
            stack.append(i)
        return ans
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1
        return ans
# @lc code=end


#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        def search(upper = False):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] < target or (upper and nums[mid] == target):
                    left = mid + 1
                else:
                    right = mid
            return left
        lower_bound = search()
        if lower_bound >= len(nums) or nums[lower_bound] != target:
            return [-1, -1]
        return [lower_bound, search(True) - 1]

# @lc code=end


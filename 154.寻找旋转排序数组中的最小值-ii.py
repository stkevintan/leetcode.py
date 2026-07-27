#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            # mid 不可能等于 right，否则 left == right 不满足 while  left < right
            # 但是不能right = mid 因为最小值可能在 mid ~ right 之间
            # [3, 3, 1, 3, 3]
            #     ↑        ↑
            #     mid      right
            if nums[mid] == nums[right]:
                right -= 1
                continue
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
        
# @lc code=end


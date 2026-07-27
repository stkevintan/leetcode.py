#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# see also leetcode 81
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid

            # 步骤 1：判断哪一半是有序的
            if nums[left] <= nums[mid]:          # 左半有序
                # 步骤 2：target 在有序这边吗？
                if nums[left] <= target < nums[mid]:
                    right = mid - 1              # 在 → 搜左边
                else:
                    left = mid + 1               # 不在 → 搜右边
            else:                                 # 右半有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1               # 在 → 搜右边
                else:
                    right = mid - 1              # 不在 → 搜左边
        return -1
# @lc code=end


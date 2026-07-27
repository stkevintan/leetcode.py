#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List

# [2,1]\n
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            # 跟右边比能够 cover 当前数组旋转与否两种情况
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def findMin1(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 
        while left < right:
            mid = (left + right) >> 1
            # 跟左边比，先需要排除当前left - right 是顺序的情况
            if nums[left] < nums[right]:
                return nums[left]
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid 

        return nums[left]
        
# @lc code=end


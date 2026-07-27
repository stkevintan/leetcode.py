#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m  = len(nums1), len(nums2)
        # 对于 nums1 可以取 0 ～ n 个
        def findMid():
            left, right = 0, n + 1
            while left < right:
                mid = (left + right) >> 1
                # nums2个数
                mid2 = (n + m) // 2 - mid
                if mid2 < 0:
                    right = mid
                elif mid2 > m:
                    left = mid + 1
                elif 0 < mid and mid2 < m and nums1[mid - 1] > nums2[mid2]:
                    right = mid
                elif mid < n and 0 < mid2 and nums1[mid] < nums2[mid2 -  1]:
                    left = mid + 1
                else:
                    # or directly return mid, mid2
                    right = mid
            return left, (n + m) // 2 - left
        mid, mid2 = findMid()
        # 哨兵：越界的一侧取 ±∞，自然不会被 max/min 选中
        def get(nums: List[int], i: int) -> float:
            if i < 0:      return float('-inf')
            if i >= len(nums): return float('inf')
            return nums[i]

        leftMax  = max(get(nums1, mid - 1), get(nums2, mid2 - 1))
        rightMin = min(get(nums1, mid),     get(nums2, mid2))

        if (n + m) & 1:
            return rightMin
        return (leftMax + rightMin) / 2
            
# @lc code=end


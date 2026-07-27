#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        i, cnt = 0, 0
        while cnt < len(nums):
            tmp = nums[i]
            j = (i + k) % n
            while j != i:
                cur = nums[j]
                nums[j] = tmp
                cnt += 1
                tmp = cur
                j = (j + k) % n
            nums[i] = tmp
            cnt += 1
            i += 1

# @lc code=end


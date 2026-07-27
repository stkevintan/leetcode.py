#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
from typing import List


# cycle sort, any num > len(nums) must not be the answer
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] != i + 1 and nums[i] <= n:
                j = nums[i] - 1
                # cycle sort caveat: prevent TLE
                if nums[j] == nums[i]:
                    break
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

        
# @lc code=end


#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(start):
            if start == len(nums):
                ans.append(nums.copy())
                return
            for i in range(start, len(nums)):
                if i == start or nums[i] != nums[start]:
                    nums[i], nums[start] = nums[start], nums[i]
                dfs(start + 1)
                nums[i],nums[start] = nums[start], nums[i]
        dfs(0)
        return ans

        
# @lc code=end


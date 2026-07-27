#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(start):
            if start == len(nums):
                ans.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                dfs(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        dfs(0)
        return ans

        
# @lc code=end


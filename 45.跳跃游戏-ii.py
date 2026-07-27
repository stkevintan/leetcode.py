#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_right = 0
        cur_end = 0
        ans = 0
        # can be stopped when reaching n - 1 
        for i, num in enumerate(nums[:-1]):
            max_right = max(max_right, i + num)
            if i == cur_end:
                ans += 1
                cur_end = max_right
        return ans

# @lc code=end


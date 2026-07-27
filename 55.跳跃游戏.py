#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_right = 0
        for i, num in enumerate(nums):
            if i > max_right:
                return False
            max_right = max(max_right, i + num)
        return True

        
# @lc code=end


#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore 投票算法: O(n) 时间, O(1) 空间
        candidate = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

        
# @lc code=end


#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = cur_max = cur_min = nums[0]
        for num in nums[1:]:
            # 同时基于旧值计算，一行搞定
            cur_max, cur_min = (
                max(num, cur_max * num, cur_min * num),
                min(num, cur_max * num, cur_min * num)
            )
            ans = max(ans, cur_max)
        return ans
        
# @lc code=end


#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
from functools import reduce


class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = reduce(int.__xor__, nums)
        low_bit = -xor & xor
        # separate nums into two parts. one's low_bit is 1, the other one's low_bit is 0
        x1, x2 = 0, 0
        for x in nums:
            if x & low_bit:
                x1 ^= x
            else:
                x2 ^= x
        return [x1, x2]
        
   

# @lc code=end


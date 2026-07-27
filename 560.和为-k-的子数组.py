#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, sum = 0, 0
        dict = defaultdict(int)
        dict[0] = 1
        for v in nums:
            sum += v
            want = sum - k
            if want in dict:
                ans += dict[want]
            dict[sum] += 1
        return ans
# @lc code=end


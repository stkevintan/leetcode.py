#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
from collections import defaultdict


class Solution:

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        prefix = 0
        for x in nums:
            prefix += x # can be mod k: prefix = (prefix + x) % k
            r = prefix % k
            ans += cnt[r]
            cnt[r] += 1
        return ans

    # TLE
    def subarraysDivByK2(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * k for _ in range(n + 1)]
        # 使用前缀和就用这个起始条件，否则用dp[i][m] = 1
        # dp[0][0] = 1
        for i in range(1, n + 1):
            m = nums[i - 1] % k
            dp[i][m] = 1
            for j in range(k):
                p = (j + nums[i - 1]) % k
                dp[i][p] += dp[i - 1][j]

        return sum([dp[i][0] for i in range(0, n + 1)])
        
# @lc code=end


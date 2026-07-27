#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from collections import defaultdict
from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pcnt = Counter(p)
        cnt = defaultdict(int) 
        ans = []
        l, r = 0, 0
        while r < len(s):
            if s[r] not in pcnt:
                r += 1
                l = r
                cnt.clear()
                continue

            cnt[s[r]] += 1
            while cnt[s[r]] > pcnt[s[r]]:
                cnt[s[l]] -= 1
                l += 1
            if r - l + 1 == len(p):
                ans.append(l)
            r += 1

        return ans
# @lc code=end


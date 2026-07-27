#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, l = 0, 0
        prev = [-1] * 128
        for (r, c) in enumerate(s):
            d = ord(c) 
            if prev[d] == -1:
                ans = max(ans, r - l + 1)
            else:
                while l < prev[d] + 1:
                    prev[ord(s[l])] = -1
                    l+=1
            prev[d] = r
        return ans

# @lc code=end


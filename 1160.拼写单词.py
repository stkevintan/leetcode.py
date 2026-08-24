#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        sum = 0
        cnt = Counter(chars)
        for w in words:
            for c, num in Counter(w).items():
                if c not in cnt or cnt[c] < num:
                    break
            else:
                sum += len(w)

        return sum


        
# @lc code=end


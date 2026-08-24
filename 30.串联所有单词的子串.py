#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        word_cnt = Counter(words)
        ans = []
        for i in range(word_len):
            left = i
            right = i
            wcnt = word_cnt.copy()
            while True:
                right += word_len
                if right > len(s):
                    break
                sub = s[right - word_len: right]
                if sub not in wcnt:
                    wcnt = word_cnt.copy()
                    left = right
                    continue
                while wcnt[sub] == 0:
                    sub1 = s[left: left + word_len]
                    wcnt[sub1] += 1
                    left += word_len
                wcnt[sub] -= 1
                if right - left == len(words) * word_len:
                    ans.append(left)
                    # step one word of left
                    wcnt[s[left: left+ word_len]] += 1
                    left += word_len

        return ans

# @lc code=end


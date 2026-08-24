#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = list(s)
        j = 0
        for i in range(len(s_arr)):
            if s_arr[i] == " " and (i == 0 or s_arr[i - 1] == " "):
                continue
            s_arr[j] = s_arr[i]
            j += 1

        while 0 < j <= len(s_arr) and s_arr[j - 1] == " ":
            j -= 1

        del s_arr[j:]

        def reverse(i, j):
            while i < j:
                s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
                i += 1
                j -= 1 
        # rotate all the string
        reverse(0, len(s_arr) - 1)

        # rotate word back
        i, j = 0, 0
        while i < len(s_arr) and j < len(s_arr):
            while j < len(s_arr) and s_arr[j] != " ": j += 1
            reverse(i, j - 1)
            i = j = j + 1
        return "".join(s_arr)




        
# @lc code=end


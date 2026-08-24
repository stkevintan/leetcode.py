#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        def go_next():
            nonlocal ans
            nxt: list[str] = []
            i = 0
            while i < len(ans):
                char = ans[i]
                cnt = 1
                while i + 1 < len(ans) and ans[i + 1] == ans[i]:
                    i += 1
                    cnt += 1
                i += 1
                nxt.append(f"{cnt}{char}")
            ans = "".join(nxt)
        for _ in range(n - 1):
           go_next() 
        return ans
        
# @lc code=end


#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
from typing import List


class MinStack:

    def __init__(self):
        # (val, min_val)
        self.stack: List[tuple[int, int]] = []
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value, value))
        else:
            self.stack.append((value, min(value, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


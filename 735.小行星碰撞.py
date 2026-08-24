#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 小行星碰撞
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0 and stack[-1] < -ast:
                stack.pop()
            if not stack:
                stack.append(ast)
            elif stack[-1] < 0 or ast > 0:
                stack.append(ast)
            elif stack[-1] == -ast:
                stack.pop()
        return list(stack)

        
# @lc code=end


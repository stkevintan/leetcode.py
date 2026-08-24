#
# @lc app=leetcode.cn id=957 lang=python3
#
# [957] N 天后的牢房
#

# @lc code=start
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        if n == 0:
            return cells

        state = 0
        def compress(cells):
            state = 0
            for i, cell in enumerate(cells):
                if cell:
                    state |= 1 << i
            return state
        state = compress(cells)

        def is_occupied(state, i):
            return bool(state & (1 << i))
        
        table = []
        while True:
            next_state = 0
            for i in range(1, 7):
                if is_occupied(state, i - 1) == is_occupied(state, i + 1):
                    next_state |= 1 << i
            # print(k, next_state)
            if table and next_state == table[0]:
                break
            table.append(next_state)
            state = next_state

        n = (n - 1) % len(table) 
        state = table[n]
        return [1 if is_occupied(state, i) else 0 for i in range(0, 8)]
            
    

# @lc code=end


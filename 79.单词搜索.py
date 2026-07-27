#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import List
from collections import Counter



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])
        # 根据词频提前剪枝
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        if any(board_count[c] < word_count[c] for c in word_count):
            return False

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        vis = [[False] * m for _ in range(n)]
        def dfs(index: int, point: tuple[int, int]):
            if index == len(word):
                return True
            for dir in dirs:
                x = point[0] + dir[0]
                y = point[1] + dir[1]
                if 0 <= x < n and 0 <= y < m and not vis[x][y] and board[x][y] == word[index]:
                    vis[x][y] = True
                    if dfs(index + 1, (x, y)):
                        # vis[x][y] = False
                        return True
                    vis[x][y] = False

            return False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    vis[i][j] = True
                    if dfs(1, (i, j)):
                        return True
                    vis[i][j] = False
        return False
        
# @lc code=end


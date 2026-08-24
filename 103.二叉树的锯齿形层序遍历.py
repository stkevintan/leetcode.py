from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque[TreeNode]()
        q.append(root)
        order = 1
        ans: List[List[int]] = []
        while q:
            row = deque[int]()
            for _ in range(len(q)):
                node = q.popleft()
                if order == 1:
                    row.append(node.val)
                else:
                    row.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(list(row)) 
            order = -order
        return ans

# @lc code=end


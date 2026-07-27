#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        q = deque()
        dt = {}
        q.append((root, 0))
        maxDepth = 0
        while len(q):
            (node, depth)= q.popleft()
            maxDepth = max(maxDepth, depth)
            if depth in dt:
                dt[depth].append(node.val)
            else:
                dt[depth] = [node.val]
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))

        return [dt[i] for i in range(maxDepth + 1)]
        


        
# @lc code=end


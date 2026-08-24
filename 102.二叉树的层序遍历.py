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
        Q = deque[TreeNode]()
        if root == None:
            return []
        ans = []
        Q.append(root)
        while Q:
            cur = []
            for _ in range(len(Q)):
                v = Q.popleft()
                cur.append(v.val)
                if v.left:
                    Q.append(v.left)
                if v.right:
                    Q.append(v.right)
            ans.append(cur)
        return ans
                

        


        
# @lc code=end


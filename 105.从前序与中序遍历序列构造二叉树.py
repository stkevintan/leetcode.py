#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

from dataclasses import dataclass


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        root =preorder[0]
        index = inorder.index(root)
        left = self.buildTree(preorder[1: index + 1], inorder[:index])
        right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return TreeNode(root, left, right)

        
# @lc code=end


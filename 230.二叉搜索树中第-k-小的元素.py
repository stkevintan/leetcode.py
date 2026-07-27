#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def travel(root):
            if root is None:
                return
            nonlocal ans,k
            travel(root.left)
            k -= 1
            if k == 0:
                ans = root.val
                return
            travel(root.right)
        travel(root)
        return ans
        
# @lc code=end


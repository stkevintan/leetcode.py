#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(root, p, q):
            nonlocal ans
            if root is None: return False
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if left and right or (root.val == p.val or root.val == q.val) and (left or right):
                ans = root
            return left or right or root.val == p.val or root.val == q.val

        dfs(root, p, q)
        return ans
        
# @lc code=end


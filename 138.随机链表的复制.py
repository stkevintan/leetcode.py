#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# @lc code=start
"""
# Definition for a Node.
"""

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 第一遍：在原节点后面插入拷贝节点 A → A' → B → B' → C → C'
        p = head
        while p:
            p.next = Node(p.val, p.next, None)
            p = p.next.next

        # 第二遍：设置拷贝节点的 random
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        # 第三遍：分离两个链表，恢复原链表
        dummy = Node(0)
        cur = dummy
        p = head
        while p:
            cur.next = p.next
            p.next = p.next.next
            cur = cur.next
            p = p.next

        return dummy.next
        
        
            
# @lc code=end


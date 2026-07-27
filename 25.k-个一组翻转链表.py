#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        dummy = ListNode(0, head)
        root = dummy
        while True:
            pk = root
            p0 = root.next
            for _ in range(k):
                pk = pk.next
                if pk is None:
                    return dummy.next
            pknext = pk.next
            while p0.next != pknext:
                p1 = p0.next
                p0.next = p1.next
                p1.next = root.next
                root.next = p1
            root = p0



# @lc code=end


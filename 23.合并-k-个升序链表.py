#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        m = (n - 1) >> 1
        p0 = self.mergeKLists(lists[0: m + 1])
        p1 = self.mergeKLists(lists[m + 1:])
        dummy = p2 = ListNode()
        while p0 and p1:
            if p0.val < p1.val:
                p2.next = p0
                p0 = p0.next
            else:
                p2.next = p1
                p1 = p1.next
            p2 = p2.next
        p2.next = p0 if p0 else p1
        return dummy.next

        

        
# @lc code=end


#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2 = list1, list2
        p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        pr = p1 if p1 else p2
        while pr:
            p.next = pr
            p = p.next
            pr = pr.next
    
        return dummy.next

        
# @lc code=end


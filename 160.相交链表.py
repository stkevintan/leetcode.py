#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        if pa is None or pb is None:
            return None
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stepA = 0
        stepB = 0
        curA = headA
        curB = headB
        while curA:
            curA = curA.next
            stepA += 1
        while curB:
            curB = curB.next
            stepB += 1
        if stepA > stepB:
            stepA, stepB = stepB, stepA
            headA, headB = headB, headA
        offset = stepB - stepA
        while offset > 0: 
            headB = headB.next
            offset -= 1
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA
        
# @lc code=end


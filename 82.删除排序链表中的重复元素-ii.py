#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val = 0
    next: Optional[ListNode] = None

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur and cur.next:
            tmp = cur.next
            deduped = False
            while tmp.next and tmp.next.val == tmp.val:
                deduped = True
                tmp.next = tmp.next.next
            if deduped:
                cur.next = tmp.next
            else:
                cur = cur.next

        return dummy.next



        
# @lc code=end


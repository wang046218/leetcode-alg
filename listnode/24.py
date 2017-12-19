"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        尝试使用递归先，之后使用迭代
        :type head: ListNode
        :rtype: ListNode
        """
        # ---------- 递归代码测试通过59ms----
        # if head is None or head.next is None:
        #     return head
        # else:
        #     temp = head.next
        #     head.next = self.swapPairs(temp.next)
        #     temp.next = head
        #     return temp
        # -----------------------------------

        # ——---------- 迭代 --------------
        if head is None or head.next is None:
            # 如果链表没有原始或者只有一个值
            return head
        p1, p2 = head, head.next
        while p2:
            # 直接交换值就可以了,不需要改动指针传递
            p1.val, p2.val = p2.val, p1.val
            p1 = p2.next
            p2 = p1.next if p1 else None
        return head

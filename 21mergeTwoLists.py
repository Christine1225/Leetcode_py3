# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 17:00:29 2018
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
@author: Abigail
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = out= ListNode(0)

        while l1 and l2:
            cur1 = l1.val
            cur2 = l2.val
            if cur1 < cur2:
                
                out.next=l1
                l1=l1.next
            else :
                out.next=l2
                l2=l2.next
            out=out.next
        out.next = l1 or l2
        return head.next    
ss=Solution()
l1=ListNode(1)
l1.next=ListNode(2)        
l1.next.next=ListNode(4) 
l2=ListNode(1)
l2.next=ListNode(3)        
l2.next.next=ListNode(4)
ans = ss.mergeTwoLists(l1,l2)
print("ans")
while ans:
    print(ans.val)
    ans=ans.next
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:18:52 2018
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
@author: Abigail
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(-1)
        result.next = head
        
        l1 ,l2 = result,result
        n+=1
        while l1:
            l1 =l1.next
            n-=1
            if n < 0:
                l2=l2.next
#                print (l2.val)
        l2.next = l2.next.next
        return result.next
            
p= ListNode(1)
p.next = ListNode(2)
p.next.next = ListNode(3)
p.next.next.next = ListNode(4)
p.next.next.next.next = ListNode(5)
ss = Solution()
result = ss.removeNthFromEnd(p,2)
while result:
    print(result.val)
    result = result.next 
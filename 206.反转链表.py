#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (57.78%)
# Total Accepted:    42.1K
# Total Submissions: 71.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from comm import *
# @lc code=start

class Solution_A:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        逐个取出放到dummy节点之后
        """

        if not head:
            return
        if not head.next:
            return head

        dummy = p = ListNode(None)
        dummy.next = head
        p = head
        while p.next:
            tmp = p.next
            p.next = p.next.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归版本, 把链表分成两部分
        head -> others  转变成 reverseList(others) -> head
        """
        if not head or not head.next:
            return head

        others = head.next
        head.next = None
        new_head = self.reverseList(others)
        others.next = head   # 反转之后others变成尾部
        return new_head

# @lc code=end

n = build_list_node(range(5))
print(Solution().reverseList(n))


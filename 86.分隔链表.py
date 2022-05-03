# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (44.54%)
# Total Accepted:    6K
# Total Submissions: 12.9K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from comm import *
# @lc code=start


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        用一个链表 gt_head 存储大于 x 的值,
        遍历 head 将 >=x 的节点都放到 gt_head 中
        再将gt_head练到head末尾
        """
        if not head:
            return
        if not head.next:
            return head

        new_head = ptr = ListNode(None)
        ptr.next = head

        gt_head = gt_ptr = ListNode(None)

        while ptr.next:
            if ptr.next.val >= x:
                tmp = ptr.next
                ptr.next = ptr.next.next
                gt_ptr.next = tmp
                gt_ptr = gt_ptr.next
            else:
                ptr = ptr.next
        if gt_head.next:
            ptr.next = gt_head.next
            gt_ptr.next = None
        return new_head.next

# @lc code=end

if __name__ == "__main__":
    l = build_list_node([1,4,3,2,5,2])
    print(Solution().partition(l, 3))

#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (36.97%)
# Total Accepted:    10.9K
# Total Submissions: 28.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
#
# Definition for singly-linked list.

from comm import *
# @lc code=start

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next or k==0:
            return head

        new_head = p1 = p2 = ListNode(None)
        new_head.next = head
        count = k
        while count > 0:
            if not p1.next:   # k 大于链表长度, 则取余数
                count = k % (k - count)
                if count == 0:
                    return head
                p1 = new_head
            p1 = p1.next
            count -= 1

        # 将后半段放到前半段的头部
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        tmp = p2.next
        p2.next = None
        p1.next = new_head.next
        new_head.next = tmp
        return new_head.next

# @lc code=end

if __name__ == "__main__":
    l = build_list_node(range(5))
    print(Solution().rotateRight(l, 10))

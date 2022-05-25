#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (75.89%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    147.1K
# Total Submissions: 193.1K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。
#
# n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
#
#
# 示例 1：
#
#
#
#
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[1,3,5,6,2,4]
#
#
# 示例 2：
#
#
#
#
# 输入：root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# 输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]
#
#
#
#
# 提示：
#
#
# 节点总数在范围 [0, 10^4]内
# 0 <= Node.val <= 10^4
# n 叉树的高度小于或等于 1000
#
#
#
#
# 进阶：递归法很简单，你可以使用迭代法完成此题吗?
#
#

from comm import *
# @lc code=start

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class SolutionA:
    def preorder(self, root: 'Node', ret=None) -> List[int]:
        # 递归版本
        if ret is None:
            ret = []
        if not root:
            return
        ret.append(root.val)
        for i in root.children:
            self.preorder(i, ret)
        return ret

class Solution:
    def preorder(self, root: 'Node', ret=None) -> List[int]:
        # 迭代版本
        if not root:
            return
        ret = []
        stack = [root]
        while stack:
            top = stack.pop()
            ret.append(top.val)
            for i in top.children[::-1]:
                stack.append(i)
        return ret

# @lc code=end


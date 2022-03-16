#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#
# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (77.49%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    145.6K
# Total Submissions: 187.8K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
#
# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
#
#
#
# 示例 1:
#
#
#
#
# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]
#
#
# Example 2:
#
#
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[]
#
#
#
#
# 提示：
#
#
# 数中节点数在 [1, 5000] 范围内
# 1 <= Node.val <= 10^7
# root 是二叉搜索树
# 1 <= val <= 10^7
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return

        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

# @lc code=end


from comm import *
if __name__ == '__main__':
    pass

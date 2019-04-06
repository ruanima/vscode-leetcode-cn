#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.97%)
# Total Accepted:    15.6K
# Total Submissions: 34.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#
class Solution(object):
    bits = {2**i for i in range(32)}
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in Solution.bits


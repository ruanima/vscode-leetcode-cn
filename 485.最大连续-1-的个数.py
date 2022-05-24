#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (51.82%)
# Total Accepted:    10K
# Total Submissions: 19.1K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1:
#
#
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#
#
# 注意：
#
#
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
#
#
#
class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        ans = 0
        length = 0
        for i in nums:
            if i == 1:
                length += 1
            else:
                ans = max(ans, length)
                length = 0
        return max(ans, length)


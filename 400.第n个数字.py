#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Easy (31.01%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 11.2K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
#
# 注意:
# n 是正数且在32为整形范围内 ( n < 2^31)。
#
# 示例 1:
#
#
# 输入:
# 3
#
# 输出:
# 3
#
#
# 示例 2:
#
#
# 输入:
# 11
#
# 输出:
# 0
#
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
#
#
#
class Solution(object):
    def findNthDigit(self, n: int) -> int:
        """二分查找法

        """

        def func(x):
            if x == 0: return 0
            a = len(str(x))
            return x * a + a - sum(10**i for i in range(a))

        if n < 1:
            return

        left = 0
        right = 2 ** 31
        target = n
        while left < right:
            mid = (left + right)//2
            if func(mid) < target:
                left = mid + 1
            else:
                right = mid
        # print(func(left), target)
        if func(left) == target:
            return str(left)[-1]
        offset = func(left) - n
        return str(left)[-1-offset]

if __name__ == "__main__":
    s = Solution().findNthDigit(15384)
    print(s)
    s = Solution().findNthDigit(11)
    print(s)

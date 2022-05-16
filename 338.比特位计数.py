#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
# https://leetcode-cn.com/problems/counting-bits/description/
#
# algorithms
# Medium (70.63%)
# Total Accepted:    7.2K
# Total Submissions: 10.2K
# Testcase Example:  '2'
#
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
#
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]
#
# 进阶:
#
#
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
#
#
#
class Solution(object):
    def countBits(self, num: int) -> list:
        """动态规划
        1. f[x]: 数字x的1的个数; 数字x一共有n位,最后一位是0和不是0
        2. f[x] = f[x>>1] if (i&1 == 0) else f[x>>1]; 也就是 f[x] = f[x>>1] + (x&1)
        """
        f = [0] * (num+1)
        for x in range(1, num+1):
            f[x] = f[x>>1] + (x&1)
        return f

if __name__ == "__main__":
    s = Solution().countBits(5)
    print(s)

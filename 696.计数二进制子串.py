#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
# https://leetcode-cn.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (45.98%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 6.6K
# Testcase Example:  '"00110"'
#
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
#
# 重复出现的子串要计算它们出现的次数。
#
# 示例 1 :
#
#
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
#
# 请注意，一些重复出现的子串要计算它们出现的次数。
#
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
#
#
# 示例 2 :
#
#
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
#
#
# 注意：
#
#
# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。
#
#
#
class WrongSolution:
    def countBinarySubstrings(self, s: str) -> int:
        """暴力法, 超时
        """
        ret = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if (j - i) % 2 != 0:
                    continue
                sub_s = s[i:j]
                if self.is_vaild(sub_s):
                    ret.append(sub_s)
        return len(ret)

    @staticmethod
    def is_vaild(s):
        assert s
        pre = None
        change_count = 0
        zero_count = 0
        one_count = 0
        for i in s:
            if i == '0':
                zero_count += 1
            else:
                one_count += 1
            if pre is not None and i != pre:
                change_count += 1
            pre = i
        return change_count == 1 and zero_count == one_count

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """分段统计
        相邻的两个段构成子字符串的数量, 是两者长度的较小值"""

        pre_count = 0
        count = 1
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                ans += min(count, pre_count)
                pre_count = count
                count = 1
        return ans + min(count, pre_count)

if __name__ == "__main__":
    s = Solution().countBinarySubstrings("00110011")
    print(s)

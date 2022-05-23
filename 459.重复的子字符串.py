#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode-cn.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (39.89%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 14.6K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
#
# 示例 1:
#
#
# 输入: "abab"
#
# 输出: True
#
# 解释: 可由子字符串 "ab" 重复两次构成。
#
#
# 示例 2:
#
#
# 输入: "aba"
#
# 输出: False
#
#
# 示例 3:
#
#
# 输入: "abcabcabcabc"
#
# 输出: True
#
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
#
#
#

# TODO(rlj): KMP算法.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        看了评论区python一行代码高赞解答，理解了一下，给大家参考。

        一个字符串如果符合要求，则该字符串至少由2个子串组成。例：b b / abc abc

        s+s。以后，则该字符串至少由4个子串组成 bb+bb / abcabc+abcabc

        截去首尾各一个字符s[1:-1] （注：只截一个是为了判断类似本例，重复子串长度为1的情况。当重复子串长度大于1时，任意截去首尾小于等于重复子字符串长度都可）

        由于s+s组成的4个重复子串被破坏了首尾2个，则只剩下中间两个 b bb b。此时在判断中间两个子串组成是否等于s，若是，则成立。
        """
        return (s + s)[1: -1].find(s) != -1

class WrongSolution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """没看清题目, 是重复多次, 该解法只能解决重复两次的情况"""

        if len(s) % 2 != 0:
            return False

        i, j = 0, len(s) // 2
        while j < len(s):
            if s[i] != s[j]:
                return False
            i += 1
            j += 1
        return True

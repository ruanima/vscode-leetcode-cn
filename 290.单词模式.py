#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词模式
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.97%)
# Total Accepted:    5.7K
# Total Submissions: 15K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
#
#

# @lc code=start


class SolutionA(object):
    def wordPattern(self, pattern: str, string: str) -> bool:
        """
        暴力法
        """
        words = string.split()
        if len(set(pattern)) != len(set(words)):
            return False
        p_len = len(pattern)
        w_len = len(words)
        if p_len < 1 or w_len < 1 or p_len != w_len:
            return False
        for i in range(p_len-1):
            for j in range(i+1, p_len):
                if (pattern[j] == pattern[i] and words[j] != words[i]):
                    return False
        return True

class Solution(object):
    def wordPattern(self, pattern: str, string: str) -> bool:
        """
        hash法
        """

        words = string.split()
        if len(pattern) != len(words):
            return False

        mapping = {}
        order = 0
        for i in words:
            key = i + '#'  # 防止i只有一个字符的情况
            if key not in mapping:
                mapping[key] = order
                order += 1

        order = 0
        for i, j in zip(pattern, words):
            if i not in mapping:
                mapping[i] = order
                order += 1
            if mapping[i] != mapping[j + '#']:
                return False
        return True

# @lc code=end

s = Solution().wordPattern("abba", "dog cat cat dog")
print(s)

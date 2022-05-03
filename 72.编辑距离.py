#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (49.68%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 14K
# Testcase Example:  '"horse"\n"ros"'
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1:
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2:
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#
class Solution(object):
    def minDistance(self, word1: str, word2: str) -> int:
        """
        f[i][j] word1前i个字符变成word2的前j个字符需要的最小步数
        word1[i] == word2[j]:
            f[i][j]: f[i-1][j-1]
        word1[i] != word2[j]:
            min(f[i-1][j], f[i+1][j], f[i-1][j-1]) + 1   # min(插入, 删除, 替换) + 1
        """
        m, n = len(word1), len(word2)
        f = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            f[i][0] = i
        for j in range(n+1):
            f[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
        return f[m][n]


if __name__ == "__main__":
    s = Solution().minDistance(word1 = "horse", word2 = "ros")
    print(s)



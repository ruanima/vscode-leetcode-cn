#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (24.76%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 17.9K
# Testcase Example:  '"ab"\n"ba"'
#
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false
# 。
#
#
#
# 示例 1：
#
# 输入： A = "ab", B = "ba"
# 输出： true
#
#
# 示例 2：
#
# 输入： A = "ab", B = "ab"
# 输出： false
#
#
# 示例 3:
#
# 输入： A = "aa", B = "aa"
# 输出： true
#
#
# 示例 4：
#
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
#
#
# 示例 5：
#
# 输入： A = "", B = "aa"
# 输出： false
#
#
#
#
# 提示：
#
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A 和 B 仅由小写字母构成。
#
#
#
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """计数法
        可改进
        """
        if len(A) != len(B):
            return False
        if len(A) < 2:
            return False

        from collections import Counter
        set_a = Counter(A)
        set_b = Counter(B)
        if set_a != set_b:
            return False
        if len(set_a) == 1:
            return True

        cnt = 0
        for a, b in zip(A, B):
            if a != b:
                cnt += 1
        return cnt == 2 or (cnt == 0 and max(set_a.values()) >= 2)

if __name__ == "__main__":
    s = Solution().buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb")
    print(s)
    s = Solution().buddyStrings(A = "ab", B = "ab")
    print(s)


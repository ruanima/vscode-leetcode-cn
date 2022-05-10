#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (64.42%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 16K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#

from comm import *
# @lc code=start

class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        """
        统计二进制位, 只出现一次的数二进制位取余3不等于0
        """
        bits = [0 for _ in range(32)]
        flags = 0
        for num in nums:
            if num < 0:
                flags += 1
                num = abs(num)
            i = 31
            while num > 0:
                if num & 1 == 1:
                    bits[i] += 1
                num >>= 1
                i -= 1
        ans = 0
        for i in range(32):
            ans <<= 1
            if (bits[i] % 3) != 0:
                ans |= 1
        return ans if (flags % 3 == 0) else -ans

# @lc code=end


if __name__ == "__main__":
    s = Solution().singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2])
    print(s)


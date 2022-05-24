#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# https://leetcode-cn.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (34.97%)
# Likes:    339
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 83K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
#
# 注意:
#
#
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
#
#
#


# TODO(rlj): something to do.
# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        归并排序
        merge时, 右半边数组的数据如果要移动到前方, 则逆序+1
        """
        pass

# @lc code=end

from comm import *
if __name__ == '__main__':
    pass

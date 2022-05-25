#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#
# https://leetcode-cn.com/problems/distribute-candies/description/
#
# algorithms
# Easy (71.06%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    95.7K
# Total Submissions: 134.8K
# Testcase Example:  '[1,1,2,2,3,3]'
#
# Alice 有 n 枚糖，其中第 i 枚糖的类型为 candyType[i] 。Alice 注意到她的体重正在增长，所以前去拜访了一位医生。
#
# 医生建议 Alice 要少摄入糖分，只吃掉她所有糖的 n / 2 即可（n 是一个偶数）。Alice
# 非常喜欢这些糖，她想要在遵循医生建议的情况下，尽可能吃到最多不同种类的糖。
#
# 给你一个长度为 n 的整数数组 candyType ，返回： Alice 在仅吃掉 n / 2 枚糖的情况下，可以吃到糖的 最多 种类数。
#
#
#
# 示例 1：
#
#
# 输入：candyType = [1,1,2,2,3,3]
# 输出：3
# 解释：Alice 只能吃 6 / 2 = 3 枚糖，由于只有 3 种糖，她可以每种吃一枚。
#
#
# 示例 2：
#
#
# 输入：candyType = [1,1,2,3]
# 输出：2
# 解释：Alice 只能吃 4 / 2 = 2 枚糖，不管她选择吃的种类是 [1,2]、[1,3] 还是 [2,3]，她只能吃到两种不同类的糖。
#
#
# 示例 3：
#
#
# 输入：candyType = [6,6,6,6]
# 输出：1
# 解释：Alice 只能吃 4 / 2 = 2 枚糖，尽管她能吃 2 枚，但只能吃到 1 种糖。
#
#
#
#
# 提示：
#
#
# n == candyType.length
# 2 <= n <= 10^4
# n 是一个偶数
# -10^5 <= candyType[i] <= 10^5
#
#
#

from comm import *
# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """计数法"""

        uniq_count = len(set(candyType))
        if uniq_count >= len(candyType) // 2:
            return len(candyType) // 2
        return uniq_count

if __name__ == "__main__":
    s = Solution().distributeCandies([1,1,2,2,3,3])
    print(s)
    s = Solution().distributeCandies([1,1,2,3])
    print(s)
# @lc code=end


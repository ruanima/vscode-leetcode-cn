#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#
# https://leetcode-cn.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (43.21%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 3K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# 公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
#
# 返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
#
#
#
# 示例：
#
# 输入：[[10,20],[30,200],[400,50],[30,20]]
# 输出：110
# 解释：
# 第一个人去 A 市，费用为 10。
# 第二个人去 A 市，费用为 30。
# 第三个人去 B 市，费用为 50。
# 第四个人去 B 市，费用为 20。
#
# 最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
#
#
#
#
# 提示：
#
#
# 1 <= costs.length <= 100
# costs.length 为偶数
# 1 <= costs[i][0], costs[i][1] <= 1000
#
#
#

from comm import *
# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """动态规划
        f[i][a] 第i个人时, 有a个人去A城市时的费用(a<=i and a <= N)
        第i个人有两种选择:
        1. 去A, 则前面就a-1个人去了A
        f[i][a] = f[i-1][a-1] + costs[i-1][0]
        2. 去B, 则前面就a个人去了A
        f[i][a] = f[i-1][a] + costs[i-1][1]
        """
        from collections import defaultdict

        f = defaultdict(lambda :defaultdict(lambda: 0))
        N = int(len(costs)/2)
        for i in range(1, len(costs)+1):
            for a in range(0, N+1):
                if a > i:  # 走A的人数比总人数还多, 不现实
                    break
                if a == 0:   # 都走A
                    f[i][a] = f[i-1][a] + costs[i-1][1]
                elif a == i:   # 都走B
                    f[i][a] = f[i-1][a-1] + costs[i-1][0]
                else:    # A, B 都有剩余名额
                    f[i][a] = min(f[i-1][a-1] + costs[i-1][0], f[i-1][a] + costs[i-1][1])
        return f[len(costs)][N]

# @lc code=end
if __name__ == "__main__":
    s = Solution().twoCitySchedCost([[918,704],[77,778],[239,457],[284,263],[872,779],[976,416],[860,518],[13,351],[137,238],[557,596],[890,227],[548,143],[384,585],[165,54]])
    print(s)

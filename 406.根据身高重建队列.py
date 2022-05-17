#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (63.11%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 6K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#

from comm import *

# @lc code=start


class Solution(object):
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """排序法
        """
        if len(people) <= 1:
            return people
        # h代表身高, k代表插队权
        # 按身高倒序, 插队权正序; 根据插队权插到对应的位置, 不影响他前面的人的插队权
        people.sort(key=lambda x: [-x[0], x[1]])
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

# @lc code=end


if __name__ == "__main__":
    s = Solution().reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    print(s)

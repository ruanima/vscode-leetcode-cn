#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (68.43%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 40.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#

from comm import *
# @lc code=start

class Solution_A(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # from itertools import permutations

        # return list(list(i) for i in permutations(nums))
        ans = []
        def dfs(level, visited):
            if level >= len(nums):
                ans.append(list(visited))
                return
            for i in nums:
                if i not in visited:
                    visited.append(i)
                    dfs(level+1, visited)
                    visited.pop()

        if not nums:
            return []
        dfs(0, [])
        return ans

class Solution(object):
    def permute(self, nums):
        def backtrack(nums, level):
            if level == len(nums):
                ans.append(track[::])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = 1
                    track.append(nums[i])
                    backtrack(nums, level+1)
                    track.pop()
                    used[i] = 0

        if len(nums) == 0:
            return []
        ans = []
        track = []
        used = [0] * len(nums)
        backtrack(nums, 0)
        return ans

# @lc code=end

if __name__ == "__main__":
    s = Solution().permute([1,2,3])
    print(s)
    s = Solution().permute([])
    print(s)

